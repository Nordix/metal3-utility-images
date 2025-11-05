# Utility Images - AI Coding Assistant Instructions

## Project Overview

Collection of miscellaneous utility container images used by Metal3
infrastructure and testing. Includes support tools, test utilities, and
helper images that don't warrant separate repositories.

## Typical Contents

- **keepalived** - HA/VIP management for Ironic
- **Test utilities** - Images for e2e test scenarios
- **Network tools** - Debugging and network configuration helpers
- **Build utilities** - CI/CD helper images

## Structure

```text
utility-images/
├── keepalived/
│   ├── Dockerfile
│   └── scripts/
├── network-tools/
│   ├── Dockerfile
│   └── tools/
└── Makefile
```

## Build Process

Each utility has its own directory with Dockerfile:

```bash
# Build specific utility
cd keepalived
make build

# Or build all
make -C <utility-name> build
```

## Usage Patterns

**keepalived Example:**

- Provides VIP for Ironic services
- Used in HA deployments
- Configured via environment variables

**Test Utilities:**

- Helper containers for e2e tests
- Network simulation tools
- Debugging utilities

## Development

**Adding New Utility:**

1. Create directory for utility
2. Add Dockerfile and any scripts
3. Add Makefile with build target
4. Document purpose and usage
5. Add to CI build pipeline if needed

## Integration

- Used by BMO ironic-deployment
- Referenced in e2e test configurations
- Deployed alongside main components when needed

## Common Pitfalls

1. **Image Size** - Keep utilities minimal and purpose-focused
2. **Versioning** - Tag images appropriately for tracking
3. **Documentation** - Each utility should have clear usage docs
4. **Dependencies** - Minimize external dependencies for reliability

This is a catch-all repository for small, focused utilities. If a
utility grows complex, consider moving to dedicated repo.
