---
id: software.devops.tranche13.001261
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/distribution/distribution/main/README.md", "https://distribution.github.io/distribution/about/configuration/", "https://github.com/distribution/distribution"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CNCF Distribution: Arquitetura da Implementação de Referência OCI Registry e Biblioteca Core

## Em uma frase
O projeto **Distribution** (`distribution/distribution`, anteriormente conhecido como Docker Registry v2, licença Apache-2.0 na CNCF) é a implementação open-source base da **OCI Distribution Specification** que serve como motor central para registros como Docker Hub, GitHub Container Registry, GitLab Container Registry, DigitalOcean Container Registry e CNCF Harbor.

## Por que importa
Compreender a arquitetura e o modelo de configuração do Distribution é fundamental tanto para operar registros privados enxutos (`registry:3`) quanto para administrar plataformas corporativas como o Harbor e o GitLab Registry que o embutem sob o capô.

## Como funciona
O repositório fornece o binário servidor `registry` (configurado via `/etc/distribution/config.yml`) e um conjunto de bibliotecas Go para manipulação de manifestos, blobs, drivers de armazenamento e middlewares de autenticação e CDN.

## Exemplo
```bash
docker run -d -p 5000:5000 --restart=always --name registry \
  -v "$(pwd)/config.yml:/etc/distribution/config.yml:ro" \
  registry:3
curl -i http://127.0.0.1:5000/v2/
```

## Limites e trade-offs
Importar diretamente pacotes internos da biblioteca Go do `distribution/distribution` sem fixar versões exatas no `go.mod` pode quebrar compilação em atualizações, pois a documentação oficial alerta que as interfaces dessas bibliotecas são instáveis.

## Como verificar
Fixe versões exatas e imutáveis tanto da imagem `registry:3` quanto dos módulos Go e valide o endpoint `/v2/` após subir o container.

## Conexões
- [[distribution-configuracao-yaml-overrides-variaveis-ambiente-otel]] — Veja também: CNCF Distribution: Configuração YAML (/etc/distribution/config.yml), Overrides por Variáveis REGISTRY_* e OpenTelemetry.

## Fontes
- [CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)](https://raw.githubusercontent.com/distribution/distribution/main/README.md) — Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry; consultado em 2026-10-03.
- [CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)](https://distribution.github.io/distribution/about/configuration/) — README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries; consultado em 2026-10-03.
- [CNCF Distribution — Official GitHub Repository](https://github.com/distribution/distribution) — Repositório oficial do CNCF Distribution; consultado em 2026-10-03.
