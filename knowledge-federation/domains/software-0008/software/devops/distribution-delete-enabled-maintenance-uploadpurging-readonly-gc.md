---
id: software.devops.tranche13.001264
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

# CNCF Distribution: Deleção de Manifestos (delete.enabled), Limpeza de Uploads (uploadpurging) e Modo Readonly para GC

## Em uma frase
No CNCF Distribution, a exclusão de tags e manifestos via API HTTP (`DELETE /v2/<name>/manifests/<reference>`) vem desabilitada por padrão (`storage.delete.enabled: false`), e a manutenção do armazenamento combina expurgo automático de uploads incompletos (`maintenance.uploadpurging`) com o modo `maintenance.readonly` para execução segura de Garbage Collection.

## Por que importa
Quando um `docker push` é interrompido por queda de rede no meio do envio de uma camada grande, arquivos temporários ficam acumulados na pasta `_uploads` se o `uploadpurging` não estiver ativo.

## Como funciona
Habilitando `storage.delete.enabled: true`, clientes autorizados podem remover referências de manifestos; `maintenance.uploadpurging` (`enabled: true`, `age: 168h`, `interval: 24h`) limpa automaticamente uploads abandonados há mais de 7 dias; e `maintenance.readonly.enabled: true` bloqueia escritas temporariamente para que o comando `registry garbage-collect /etc/distribution/config.yml` remova blobs não referenciados sem condição de corrida.

## Exemplo
```yaml
storage:
  delete:
    enabled: true
  maintenance:
    uploadpurging:
      enabled: true
      age: 168h
      interval: 24h
      dryrun: false
    readonly:
      enabled: false
```

## Limites e trade-offs
Executar `registry garbage-collect` enquanto o registro está aceitando `docker push` concorrentes (`readonly.enabled: false`) pode apagar o blob de uma camada que acabou de ser enviada mas cujo manifesto ainda não foi finalizado, corrompendo a imagem.

## Como verificar
Ative `readonly.enabled: true` (ou execute em janela sem pushes) antes de rodar `registry garbage-collect` e use `--dry-run` para revisar o plano de limpeza.

## Conexões
- [[distribution-storage-drivers-filesystem-s3-gcs-azure-inmemory]] — Veja também: CNCF Distribution: Drivers de Armazenamento (filesystem, s3, gcs, azure e inmemory) e Parâmetros de Performance.
- [[distribution-autenticacao-htpasswd-token-jwt-jwks-mtls]] — Veja também: CNCF Distribution: Autenticação com htpasswd, Token Server Externo (JWT/JWKS) e mTLS.

## Fontes
- [CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)](https://distribution.github.io/distribution/about/configuration/) — Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry; consultado em 2026-10-03.
- [CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)](https://raw.githubusercontent.com/distribution/distribution/main/README.md) — README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries; consultado em 2026-10-03.
- [CNCF Distribution — Official GitHub Repository](https://github.com/distribution/distribution) — Repositório oficial do CNCF Distribution; consultado em 2026-10-03.
