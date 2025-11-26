Workend on manua deployment but failed on automated trigger 

1.  **Block 1: "Internal Error "**[1]
    *   **Cause:** `storage-admin` couldn't "act as" the App Engine runtime identity (`kubes-475406@appspot...`).
    *   **Fix:** You added `roles/iam.serviceAccountUser`.

2.  **Block 2: "Cannot write logs"**
    *   **Cause:** `storage-admin` had zero rights to write to Cloud Logging.
    *   **Fix:** You added `roles/logging.logWriter`.

3.  **Block 3: "Promoting version failed"**
    *   **Cause:** `storage-admin` had permission to *upload* code (`Deployer`), but not to *switch traffic* (`Service Admin`) to it.
    *   **Fix:** You added `roles/appengine.serviceAdmin`.

### Conclusion
The only problem was that **custom service accounts start with nothing**. You have to manually build their "keychain" of permissions. Now that you've given it the keys to the car (Logging, Deploying, Traffic Switching), the automatic deployment works just as well as your manual one.
