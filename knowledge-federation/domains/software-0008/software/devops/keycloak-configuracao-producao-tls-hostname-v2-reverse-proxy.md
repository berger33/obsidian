---
id: software.devops.tranche11.001002
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
fontes: ["https://www.keycloak.org/server/configuration-production", "https://www.keycloak.org/guides", "https://raw.githubusercontent.com/keycloak/keycloak/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Keycloak em produção: TLS, Hostname v2, separação da URL administrativa e configuração de Reverse Proxy

## Em uma frase
A preparação do Keycloak para produção (`kc.sh start`) exige canais criptografados com TLS, configuração explícita do Hostname v2 diferenciando URLs públicas de frontend das URLs de administração/backchannel e integração adequada com proxies reversos ou balanceadores de carga.

## Por que importa
Em ambientes corporativos, as instâncias do Keycloak rodam em sub-redes privadas atrás de Ingress Controllers ou API Gateways. Sem separar o hostname público de login da interface administrativa (`Admin REST API` e `Admin Console`), toda a superfície de gerenciamento do IAM fica exposta à internet pública, ampliando o risco de ataques contra credenciais administrativas.

## Como funciona
Segundo o guia oficial *Configuring Keycloak for production*, o operador deve: (1) habilitar HTTPS/TLS para tráfego de entrada, requisições HTTP de saída e tráfego de cache entre nós; (2) configurar o **Hostname (v2)** (`--hostname` e `--hostname-admin`) para expor os fluxos públicos de login em um domínio público (ex.: `auth.exemplo.com`) enquanto restringe a Admin Console e a Admin REST API a um hostname administrativo interno ou bloqueia seus caminhos na camada do reverse proxy; e (3) configurar os cabeçalhos de encaminhamento do reverse proxy (`--proxy-headers xforwarded` ou `forwarded`) para que o Keycloak reconheça o IP real do cliente e o esquema HTTPS.

## Exemplo
```bash
# Iniciar o Keycloak em modo de produção separando o hostname público de login do hostname administrativo interno
bin/kc.sh start \
  --hostname=https://auth.exemplo.com \
  --hostname-admin=https://admin-auth.interno.exemplo.com \
  --proxy-headers=xforwarded \
  --https-certificate-file=/etc/x509/https/tls.crt \
  --https-certificate-key-file=/etc/x509/https/tls.key
```

## Limites e trade-offs
Quando `--proxy-headers` está habilitado no Keycloak, o servidor passa a confiar nos cabeçalhos `X-Forwarded-*` ou `Forwarded` recebidos; portanto, o firewall ou a NetworkPolicy do Kubernetes deve garantir que apenas o Ingress Controller / Reverse Proxy confiável consiga alcançar a porta HTTP/HTTPS dos pods do Keycloak.

## Como verificar
Inspecione o JSON retornado em `https://auth.exemplo.com/realms/master/.well-known/openid-configuration` para confirmar que os endpoints públicos usam `https://auth.exemplo.com` e verifique no reverse proxy que `/admin` retorna bloqueio a partir da rede pública.

## Conexões
- [[keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf]] — Veja também: Keycloak: plataforma open-source CNCF de gerenciamento de identidade e acesso (IAM) com OpenID Connect, OAuth 2.0 e SAML 2.0.
- [[keycloak-protecao-sobrecarga-queued-requests-async-bootstrap]] — Veja também: Keycloak: proteção contra sobrecarga (http-max-queued-requests) e inicialização assíncrona (--server-async-bootstrap).
- [[keycloak-cluster-alta-disponibilidade-infinispan-jgroups-banco]] — Referência cruzada direta com keycloak-cluster-alta-disponibilidade-infinispan-jgroups-banco.

## Fontes
- [Keycloak Official Documentation — Configuring Keycloak for production & Guides](https://www.keycloak.org/server/configuration-production) — Guias oficiais de configuração do Keycloak para produção (TLS, Hostname v2, reverse proxy, http-max-queued-requests, --server-async-bootstrap, JGroups/Infinispan, Operator, OpenTelemetry e especificações modernas); consultado em 2026-10-03.
- [Keycloak GitHub — README.md & Official Documentation Portal](https://www.keycloak.org/guides) — README oficial do projeto CNCF keycloak/keycloak (Apache-2.0) e índice de guias de servidor, operator, observabilidade e segurança de aplicações; consultado em 2026-10-03.
- [Keycloak — Official Guides & Server Reference](https://raw.githubusercontent.com/keycloak/keycloak/main/README.md) — Portal oficial de guias do Keycloak; consultado em 2026-10-03.
