# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New feature development that is not yet released.

## [1.0.0] - 2025-09-15

### Added
- **Public Launch!** The initial public release of the platform.
- User authentication with email/password and JWT.
- Core CRUD functionality for projects and tasks.
- Real-time analytics dashboard for admin users.
- REST API with OpenAPI 3.0 documentation.
- Comprehensive test suite with 90%+ code coverage.

### Changed
- Upgraded backend framework to FastAPI 0.100.0 for performance improvements.
- Refactored database schema to better support future features.

### Fixed
- Resolved issue where password reset tokens were not expiring correctly.
- Patched a memory leak in the background worker service.

## [0.1.0] - 2025-06-15

### Added
- **Closed Beta Release.**
- Initial infrastructure setup on AWS using Terraform.
- CI/CD pipeline with GitHub Actions for automated testing and deployment.
