---
id: software.devops.tranche12.001142
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://nova.docs.fairwinds.com/quickstart/", "https://nova.docs.fairwinds.com/usage/", "https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds Nova: Auditoria de Imagens de Containers Desatualizadas com --containers

## Em uma frase
Além de releases Helm, o comando `nova find --containers` (ou combinado como `nova find --helm --containers`) inspeciona os Pods em execução no cluster Kubernetes e consulta os registros de containers remotos para identificar tags de imagem desatualizadas em relação à última versão major (`Latest`), minor (`Latest Minor`) e patch (`Latest Patch`).

## Por que importa
Nem toda carga de trabalho no cluster é instalada via Helm: componentes do control plane (`coredns`, `etcd`, `kube-apiserver`), operadores instalados por YAML estático e microsserviços próprios podem rodar imagens com patches de segurança atrasados há meses.

## Como funciona
Quando executado com `--containers`, o Nova enumera as imagens em execução nos namespaces selecionados, analisa as tags que seguem versionamento semântico (SemVer) e consulta o registry correspondente (com timeout configurável via `--timeout`, padrão 10s), classificando separadamente a atualização mais recente de patch, minor e major.

## Exemplo
```bash
nova find --containers --format table
nova find --helm --containers --namespace kube-system --format json
```

## Limites e trade-offs
Executar `nova find --containers` esperando que tags mutáveis ou baseadas apenas em hash Git (`latest`, `main`, `sha-8f3a1b`) apareçam por padrão no relatório de versões ignora esses containers, pois o Nova filtra tags não-SemVer por padrão.

## Como verificar
Use tags SemVer imutáveis nas imagens do cluster e, durante auditorias abrangentes, adicione `--show-non-semver` e `--show-errored-containers` para visibilidade completa.

## Conexões
- [[nova-auditoria-helm-charts-desatualizados-depreciados-find]] — Veja também: Fairwinds Nova: Detecção de Helm Charts Desatualizados e Depreciados no Cluster (nova find).
- [[nova-repositorios-helm-privados-artifacthub-poll-url]] — Veja também: Fairwinds Nova: Uso com Repositórios Helm Privados (--url e --poll-artifacthub=false).

## Fontes
- [Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)](https://nova.docs.fairwinds.com/quickstart/) — README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova; consultado em 2026-10-03.
- [Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)](https://nova.docs.fairwinds.com/usage/) — Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON; consultado em 2026-10-03.
- [Fairwinds Nova — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md) — Portal oficial de documentação do Fairwinds Nova; consultado em 2026-10-03.
