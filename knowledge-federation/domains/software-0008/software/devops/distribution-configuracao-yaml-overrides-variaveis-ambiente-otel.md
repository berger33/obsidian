---
id: software.devops.tranche13.001262
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
fontes: ["https://distribution.github.io/distribution/about/configuration/", "https://raw.githubusercontent.com/distribution/distribution/main/README.md", "https://github.com/distribution/distribution"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CNCF Distribution: Configuração YAML (/etc/distribution/config.yml), Overrides por Variáveis REGISTRY_* e OpenTelemetry

## Em uma frase
O servidor Distribution é configurado por um arquivo YAML (`version: 0.1` em `/etc/distribution/config.yml`) onde qualquer opção individual pode ser sobrescrita por variáveis de ambiente seguindo a convenção `REGISTRY_<CAMINHO_EM_MAIUSCULAS>` (com `_` representando níveis de indentação e índices numéricos `_0` para listas), além de controlar exportação de traces via `OTEL_TRACES_EXPORTER`.

## Por que importa
Ao implantar o registry em Kubernetes ou Docker, injetar segredos (como chaves S3, senhas de Redis ou `http.secret`) ou ajustar um diretório sem reconstruir a imagem exige usar variáveis de ambiente previsíveis.

## Como funciona
Por exemplo, `storage.filesystem.rootdirectory` torna-se `REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY=/somewhere`, e o primeiro item da lista `http.tls.letsencrypt.hosts` torna-se `REGISTRY_HTTP_TLS_LETSENCRYPT_HOSTS_0=registry.example.com`. Como o exportador de traces padrão aponta para `https://localhost:4318/v1/traces`, define-se `OTEL_TRACES_EXPORTER=none` quando não há coletor OpenTelemetry local.

## Exemplo
```bash
docker run -d -p 5000:5000 --name registry \
  -e REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY=/var/lib/registry \
  -e REGISTRY_STORAGE_DELETE_ENABLED=true \
  -e OTEL_TRACES_EXPORTER=none \
  registry:3
```

## Limites e trade-offs
Esquecer de definir `OTEL_TRACES_EXPORTER=none` em ambientes onde não existe um coletor OpenTelemetry escutando em `localhost:4318` polui os logs do container com erros periódicos de falha de conexão de exportação de traces.

## Como verificar
Defina `OTEL_TRACES_EXPORTER=none` (ou aponte para o endpoint OTLP real do cluster) e mantenha um `config.yml` base claro, usando variáveis `REGISTRY_*` apenas para segredos e ajustes pontuais.

## Conexões
- [[distribution-arquitetura-oci-registry-v2-core-library-cncf]] — Veja também: CNCF Distribution: Arquitetura da Implementação de Referência OCI Registry e Biblioteca Core.
- [[distribution-storage-drivers-filesystem-s3-gcs-azure-inmemory]] — Veja também: CNCF Distribution: Drivers de Armazenamento (filesystem, s3, gcs, azure e inmemory) e Parâmetros de Performance.

## Fontes
- [CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)](https://distribution.github.io/distribution/about/configuration/) — Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry; consultado em 2026-10-03.
- [CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)](https://raw.githubusercontent.com/distribution/distribution/main/README.md) — README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries; consultado em 2026-10-03.
- [CNCF Distribution — Official GitHub Repository](https://github.com/distribution/distribution) — Repositório oficial do CNCF Distribution; consultado em 2026-10-03.
