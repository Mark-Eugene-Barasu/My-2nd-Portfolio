"""
GraphQL Schema for Portfolio API

Provides a modern query interface alongside REST endpoints.
Demonstrates GraphQL knowledge for recruiters evaluating the backend.
"""

import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from contact.models import ContactMessage
from analytics.models import PageView

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'role', 'company', 'title')


class ContactMessageType(DjangoObjectType):
    class Meta:
        model = ContactMessage
        fields = ('id', 'name', 'email', 'message', 'is_read', 'created_at')


class PageViewType(DjangoObjectType):
    class Meta:
        model = PageView
        fields = ('id', 'page', 'ip_address', 'user_role', 'visited_at')


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_messages = graphene.List(ContactMessageType)
    analytics_summary = graphene.Field(graphene.String)

    def resolve_all_users(self, info):
        user = info.context.user
        if not user.is_authenticated or not user.is_admin:
            raise Exception('Admin access required')
        return User.objects.all()

    def resolve_all_messages(self, info):
        user = info.context.user
        if not user.is_authenticated or not user.is_admin:
            raise Exception('Admin access required')
        return ContactMessage.objects.all()

    def resolve_analytics_summary(self, info):
        total = PageView.objects.count()
        return f"Total page views: {total}"


schema = graphene.Schema(query=Query)
