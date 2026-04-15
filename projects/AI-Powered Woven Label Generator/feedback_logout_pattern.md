---
name: Griffes Vivienne — logout must go through useAuth.logout()
description: Never create a local tRPC auth.logout mutation in components — it skips clerk.signOut() and breaks logout
type: feedback
---

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[sessions/session-2026-04-15-griffes-vivienne-conversion-polish|Conversion polish session]]

Always use `useAuth().logout()` for logout actions. Never call `trpc.auth.logout.useMutation()` directly from a component.

**Why:** `useAuth.logout()` in `client/src/_core/hooks/useAuth.ts` runs three steps in a `finally` block:
1. `trpc.auth.logout` (server session)
2. `clerk.signOut()` ← **this is what actually ends the Clerk session**
3. `utils.auth.me.invalidate()` (cache flush)

Calling only the tRPC mutation (step 1) leaves the Clerk token alive. The user is redirected to `/`, but Clerk silently re-authenticates them on the next request. The page looks like logout worked, but it didn't.

**How to apply:** In any component that needs logout, destructure `logout` from `useAuth()`:
```ts
const { user, isAuthenticated, logout } = useAuth();

const handleLogout = async () => {
  await logout();
  toast.success("Logged out");
  setLocation("/");
};
```
