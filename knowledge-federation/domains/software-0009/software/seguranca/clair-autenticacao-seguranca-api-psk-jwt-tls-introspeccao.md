---
id: software.seguranca.tranche07.000698
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://quay.github.io/clair/whatis.html", "https://raw.githubusercontent.com/quay/clair/main/README.md", "https://quay.github.io/claircore/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Clair v4: Hardening da API — Autenticação **JWT com Pre-Shared Key (`auth.psk`)**, TLS Mútuo e Isolamento da Porta de Introspecção

## Em uma frase
Como a API do `Indexer` recebe URLs e cabeçalhos `Authorization` para baixar blobs de imagens privadas, e a API do `Matcher` expõe todo o inventário de vulnerabilidades das aplicações da empresa, a comunicação com o Clair v4 em produção deve ser autenticada via **JWT (`auth.psk`)** sobre **TLS**.

## Por que importa
O bloco **`auth.psk`** no `config.yaml` configura o Clair v4 para exigir em todas as requisições HTTP (exceto na porta interna de healthcheck/metrics) um cabeçalho `Authorization: Bearer <JWT>` assinado com algoritmo HMAC (`HS256`/`HS384`/`HS512`) usando a chave compartilhada Base64 configurada em `key` e validando o emissor na lista `iss` (ex.: `["quay", "ci-scanner"]`).

## Como funciona
Além disso, a porta de introspecção (`introspection_addr: "127.0.0.1:8089"`, que expõe `/healthz`, `/readyz`, `/metrics` Prometheus e perfis `/debug/pprof/`) deve ficar restrita ao loopback ou à NetworkPolicy exclusiva do Prometheus, nunca exposta no Ingress.

## Exemplo
```yaml
# Configuracao de autenticacao JWT por Pre-Shared Key (PSK) no config.yaml do Clair v4
auth:
  psk:
    key: "dGhpcy1pcy1hLTI1Ni1iaXQtc2VjcmV0LWtleS1pbi1iYXNlNjQ="
    iss:
      - "quay-registry-prod"
      - "secops-clairctl"
tls:
  cert: "/etc/clair/tls/clair-server.crt"
  key: "/etc/clair/tls/clair-server.key"
```

## Limites e trade-offs
Quando o Clair v4 roda em modo de microsserviços separados (`indexer`, `matcher`, `notifier`) com `auth.psk` habilitado, o próprio `Matcher` e o `Notifier` usam automaticamente a primeira string listada em `auth.psk.iss` para assinar suas chamadas internas ao `Indexer`!

## Como verificar
Teste fazer uma requisição sem token JWT para `https://clair.internal.corp:6060/indexer/api/v1/index_state` e confirme que o Clair retorna `HTTP 401 Unauthorized`.

## Conexões
- [[clair-implantacao-combo-vs-microservicos-postgresql-escalabilidade]] — Veja também: Clair v4: Modos de Implantação (`combo` vs Microsserviços `indexer`/`matcher`/`notifier`), Dimensionamento de PostgreSQL e Coordenação via `clair-lock`.
- [[clair-enriquecimento-cvss-severidade-normalizada-priorizacao-remediacao]] — Veja também: Clair v4: Normalização de Severidade (`Unknown`, `Negligible`, `Low`, `Medium`, `High`, `Critical`), Enriquecimento CVSS e Priorização.
- [[clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier]] — Referência cruzada direta com clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier.
- [[testssl-auditoria-protocolos-tls12-tls13-quic-alpn-npn]] — Referência cruzada direta com testssl-auditoria-protocolos-tls12-tls13-quic-alpn-npn.

## Fontes
- [Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture](https://quay.github.io/clair/whatis.html) — documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier; consultado em 2026-10-03.
- [Project Quay Clair Official GitHub — Container Vulnerability Static Analysis](https://raw.githubusercontent.com/quay/clair/main/README.md) — repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl; consultado em 2026-10-03.
- [ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine](https://quay.github.io/claircore/) — documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades; consultado em 2026-10-03.
