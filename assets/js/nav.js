/**
 * Nav.js — Dynamic Navigation based on Authentication & Role
 * 
 * Injects login/logout link, admin dashboard link, and user greeting.
 */

function updateNav() {
  const navContainer = document.getElementById('navLinks');
  if (!navContainer) return;

  const authItem = document.getElementById('authNavItem');
  if (!authItem) return;

  if (Auth.isAuthenticated()) {
    const user = Auth.getUser();
    const roleLabel = user ? ` (${user.role})` : '';

    // Replace login link with user menu
    authItem.innerHTML = `
      <a href="#" onclick="Auth.logout().then(() => location.reload()); return false;" title="Logout">
        <i class="fas fa-sign-out-alt"></i> Logout${roleLabel}
      </a>
    `;

    // Inject admin link if admin
    if (Auth.isAdmin() && !document.getElementById('adminNavItem')) {
      const adminLi = document.createElement('li');
      adminLi.id = 'adminNavItem';
      adminLi.innerHTML = `<a href="${API_BASE}/admin/" target="_blank"><i class="fas fa-cog"></i> Admin</a>`;
      navContainer.insertBefore(adminLi, authItem);
    }

    // Update contact form user info if present
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    if (nameInput && user && user.first_name) {
      nameInput.value = `${user.first_name} ${user.last_name || ''}`.trim();
      nameInput.readOnly = true;
    }
    if (emailInput && user && user.email) {
      emailInput.value = user.email;
      emailInput.readOnly = true;
    }
  } else {
    authItem.innerHTML = `<a href="#" onclick="openLoginModal(); return false;"><i class="fas fa-sign-in-alt"></i> Login</a>`;
    const adminLi = document.getElementById('adminNavItem');
    if (adminLi) adminLi.remove();
  }
}

// Listen for auth changes
window.addEventListener('authchange', () => setTimeout(updateNav, 100));

// Run on page load
document.addEventListener('DOMContentLoaded', updateNav);
