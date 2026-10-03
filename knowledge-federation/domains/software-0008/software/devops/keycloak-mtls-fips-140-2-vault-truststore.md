---
id: software.devops.tranche11.001008
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://www.keycloak.org/guides", "https://www.keycloak.org/server/configuration-production", "https://raw.githubusercontent.com/keycloak/keycloak/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Segurança corporativa no Keycloak: mTLS, conformidade FIPS 140-2, Truststore e integração com Vault

## Em uma frase
Para ambientes regulados e de alta segurança, o Keycloak suporta autenticação mútua TLS (**mTLS**) para verificar certificados X.509 de clientes, operação em modo de conformidade **FIPS 140-2**, gerenciamento centralizado de certificados confiáveis (**Truststore**) e leitura segura de segredos externos via **Vault**.

## Por que importa
No setor financeiro, governamental e de saúde, aplicações machine-to-machine (como Open Banking / FAPI) exigem autenticação de cliente baseada em certificado mTLS (`tls_client_auth`) e módulos criptográficos validados sob FIPS 140-2, além de proibir senhas de banco de dados ou chaves SMTP em texto claro nos arquivos de configuração.

## Como funciona
Conforme detalham os guias de servidor (`keycloak.org/guides`), o administrador pode: (1) configurar **Mutual TLS (mTLS)** (`--https-client-auth=request` ou `required`) junto ao **Keycloak Truststore** (`--truststore-paths`) para validar certificados de clientes que se conectam ao Keycloak e certificados TLS de serviços externos (como LDAPS ou provedores OIDC); (2) habilitar o modo **FIPS 140-2** (`--fips-mode=non-strict` ou `strict`) utilizando provedores criptográficos BouncyCastle FIPS; e (3) configurar um **Vault** no Keycloak (ex.: Kubernetes Secrets montados em arquivos ou integrações de cofre) referenciando segredos por expressões `${vault.ID}` em vez de strings literais.

## Exemplo
```bash
# Iniciar o Keycloak exigindo ou solicitando certificados mTLS de clientes e carregando certificados confiáveis na Truststore
bin/kc.sh start \
  --https-client-auth=request \
  --truststore-paths=/etc/keycloak/truststore/ca-bundle.pem \
  --vault=file \
  --vault-dir=/var/run/secrets/keycloak-vault
```

## Limites e trade-offs
Em modo `--fips-mode=strict`, algoritmos criptográficos legados, tamanhos de chave curtos e formatos de keystore não aprovados pelo padrão FIPS (como JKS tradicionais em vez de BCFKS/PKCS12 compatíveis) são rejeitados imediatamente na inicialização ou durante o handshake TLS.

## Como verificar
Teste a conexão mTLS contra o endpoint de token usando `curl --cert client.crt --key client.key --cacert ca.pem https://auth.exemplo.com/realms/corp/protocol/openid-connect/token` para validar a aceitação do certificado de cliente.

## Conexões
- [[keycloak-padroes-modernos-seguranca-dpop-token-exchange-mcp]] — Veja também: Padrões avançados no Keycloak: DPoP, Token Exchange, JWT Authorization Grant, AuthZEN, SSF e servidores MCP.
- [[keycloak-automacao-admin-rest-api-cli-export-import-realms]] — Veja também: Automação no Keycloak: Admin REST API, Admin Client, registro de clientes via CLI e importação/exportação de Realms.
- [[keycloak-configuracao-producao-tls-hostname-v2-reverse-proxy]] — Referência cruzada direta com keycloak-configuracao-producao-tls-hostname-v2-reverse-proxy.
- [[vault-gerenciamento-centralizado-segredos-arquitetura-acesso]] — Referência cruzada direta com vault-gerenciamento-centralizado-segredos-arquitetura-acesso.

## Fontes
- [Keycloak Official Documentation — Configuring Keycloak for production & Guides](https://www.keycloak.org/guides) — Guias oficiais de configuração do Keycloak para produção (TLS, Hostname v2, reverse proxy, http-max-queued-requests, --server-async-bootstrap, JGroups/Infinispan, Operator, OpenTelemetry e especificações modernas); consultado em 2026-10-03.
- [Keycloak GitHub — README.md & Official Documentation Portal](https://www.keycloak.org/server/configuration-production) — README oficial do projeto CNCF keycloak/keycloak (Apache-2.0) e índice de guias de servidor, operator, observabilidade e segurança de aplicações; consultado em 2026-10-03.
- [Keycloak — Official Guides & Server Reference](https://raw.githubusercontent.com/keycloak/keycloak/main/README.md) — Portal oficial de guias do Keycloak; consultado em 2026-10-03.
