curl \
    -H "X-Vault-Token: $VAULT_TOKEN" \
    -H "Content-Type: application/json" \
    -X POST \
    -d '{"data":{"value":"bar"}}' \
    https://vault.openknowit.com/v1/secrets/kv/test

