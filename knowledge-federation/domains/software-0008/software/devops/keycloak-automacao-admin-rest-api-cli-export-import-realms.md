---
id: software.devops.tranche11.001009
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

# Automação no Keycloak: Admin REST API, Admin Client, registro de clientes via CLI e importação/exportação de Realms

## Em uma frase
O Keycloak permite automatizar integralmente o provisionamento de identidades e configurações por meio da **Keycloak Admin REST API**, das bibliotecas **Keycloak Admin Client**, do serviço de registro dinâmico de clientes via CLI e dos comandos `kc.sh import` e `kc.sh export` para serializar Realms em arquivos JSON.

## Por que importa
Em plataformas self-service (Internal Developer Platforms), quando uma equipe cria um novo microsserviço ou ambiente efêmero, o pipeline de CI/CD precisa registrar automaticamente o cliente OIDC, definir redirect URIs, atribuir roles e exportar/importar templates de realms sem intervenção humana no painel web.

## Como funciona
De acordo com a documentação oficial (`keycloak.org/guides`), existem três frentes complementares de automação: (1) **Importing and exporting realms**: o comando `bin/kc.sh export --dir /tmp/export --realm meu-realm` exporta a configuração do realm em JSON e `bin/kc.sh import --dir /tmp/export` (ou `--import-realm` no boot) carrega realms declarativos; (2) **Client Registration CLI (`kcadm.sh` / `kcreg.sh`)**: permite registrar e atualizar clientes OIDC/SAML pela linha de comando usando tokens de registro inicial; e (3) **Keycloak Admin REST API e Admin Client**: fornecem acesso programático autenticado para gerenciar usuários, grupos, roles e clientes a partir de código Go, Java, Python ou Terraform.

## Exemplo
```bash
# Exportar a configuração de um realm para um diretório JSON e importar realms automaticamente na inicialização
bin/kc.sh export --dir=/opt/keycloak/data/import --realm=plataforma --users=realm_file
bin/kc.sh start --import-realm
```

## Limites e trade-offs
Conforme alerta a documentação de produção, a **Keycloak Administration REST API** possui privilégios amplos sobre os realms; ela deve ser bloqueada no nível do reverse proxy público ou exposta apenas em um hostname interno dedicado (`--hostname-admin`), concedendo tokens de serviço com escopo mínimo por realm.

## Como verificar
Liste os arquivos JSON gerados em `/opt/keycloak/data/import` após o comando `kc.sh export` e valide nos logs de `kc.sh start --import-realm` a mensagem de importação concluída do realm.

## Conexões
- [[keycloak-mtls-fips-140-2-vault-truststore]] — Veja também: Segurança corporativa no Keycloak: mTLS, conformidade FIPS 140-2, Truststore e integração com Vault.
- [[keycloak-integracao-distribution-registry-apache-oidc-saml-adapters]] — Veja também: Integração do Keycloak com infraestrutura: Distribution Registry (OCI), Apache mod_auth_openidc / mod_auth_mellon e Adapters.
- [[keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf]] — Referência cruzada direta com keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf.
- [[keycloak-operator-kubernetes-crds-realm-import-clients]] — Referência cruzada direta com keycloak-operator-kubernetes-crds-realm-import-clients.
- [[keycloak-configuracao-producao-tls-hostname-v2-reverse-proxy]] — Referência cruzada direta com keycloak-configuracao-producao-tls-hostname-v2-reverse-proxy.

## Fontes
- [Keycloak Official Documentation — Configuring Keycloak for production & Guides](https://www.keycloak.org/guides) — Guias oficiais de configuração do Keycloak para produção (TLS, Hostname v2, reverse proxy, http-max-queued-requests, --server-async-bootstrap, JGroups/Infinispan, Operator, OpenTelemetry e especificações modernas); consultado em 2026-10-03.
- [Keycloak GitHub — README.md & Official Documentation Portal](https://www.keycloak.org/server/configuration-production) — README oficial do projeto CNCF keycloak/keycloak (Apache-2.0) e índice de guias de servidor, operator, observabilidade e segurança de aplicações; consultado em 2026-10-03.
- [Keycloak — Official Guides & Server Reference](https://raw.githubusercontent.com/keycloak/keycloak/main/README.md) — Portal oficial de guias do Keycloak; consultado em 2026-10-03.
