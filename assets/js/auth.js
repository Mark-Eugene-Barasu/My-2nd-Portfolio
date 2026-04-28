/**
 * Auth.js — JWT Authentication & Role-Based Access Control
 * 
 * Handles: login, logout, token refresh, role checking
 * Stores tokens in localStorage (or memory for higher security)
 */

const API_BASE = 'http://127.0.0.1:8000/api';

const Auth = {
  /** Get access token from storage */
  getAccessToken() {
    return localStorage.getItem('access_token');
  },

  /** Get refresh token from storage */
  getRefreshToken() {
    return localStorage.getItem('refresh_token');
  },

  /** Get parsed user object from storage */
  getUser() {
    const raw = localStorage.getItem('user');
    try { return raw ? JSON.parse(raw) : null; } catch { return null; }
  },

  /** Check if user is authenticated */
  isAuthenticated() {
    return !!this.getAccessToken();
  },

  /** Check if user has admin role */
  isAdmin() {
    const user = this.getUser();
    return user && (user.is_admin || user.role === 'ADMIN');
  },

  /** Check if user is recruiter */
  isRecruiter() {
    const user = this.getUser();
    return user && (user.is_recruiter || user.role === 'RECRUITER');
  },

  /** Get auth headers for fetch requests */
  headers() {
    const token = this.getAccessToken();
    return {
      'Content-Type': 'application/json',
      ...(token ? { 'Authorization': `Bearer ${token}` } : {})
    };
  },

  /** Login with username/password */
  async login(username, password) {
    const res = await fetch(`${API_BASE}/auth/login/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || JSON.stringify(data));

    localStorage.setItem('access_token', data.tokens.access);
    localStorage.setItem('refresh_token', data.tokens.refresh);
    localStorage.setItem('user', JSON.stringify(data.user));

    window.dispatchEvent(new Event('authchange'));
    return data;
  },

  /** Register new account */
  async register(payload) {
    const res = await fetch(`${API_BASE}/auth/register/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || JSON.stringify(data));

    localStorage.setItem('access_token', data.tokens.access);
    localStorage.setItem('refresh_token', data.tokens.refresh);
    localStorage.setItem('user', JSON.stringify(data.user));

    window.dispatchEvent(new Event('authchange'));
    return data;
  },

  /** Refresh access token */
  async refresh() {
    const refresh = this.getRefreshToken();
    if (!refresh) throw new Error('No refresh token');

    const res = await fetch(`${API_BASE}/auth/refresh/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh })
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Refresh failed');

    localStorage.setItem('access_token', data.access);
    return data.access;
  },

  /** Logout and clear storage */
  async logout() {
    const refresh = this.getRefreshToken();
    if (refresh) {
      try {
        await fetch(`${API_BASE}/auth/logout/`, {
          method: 'POST',
          headers: this.headers(),
          body: JSON.stringify({ refresh })
        });
      } catch { /* ignore */ }
    }

    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user');

    window.dispatchEvent(new Event('authchange'));
  },

  /** Fetch with automatic token refresh on 401 */
  async fetch(url, options = {}) {
    options.headers = { ...this.headers(), ...(options.headers || {}) };

    let res = await fetch(url, options);

    if (res.status === 401) {
      try {
        await this.refresh();
        options.headers = { ...this.headers(), ...(options.headers || {}) };
        res = await fetch(url, options);
      } catch {
        this.logout();
        throw new Error('Session expired. Please log in again.');
      }
    }

    return res;
  }
};

// Expose globally
window.Auth = Auth;

