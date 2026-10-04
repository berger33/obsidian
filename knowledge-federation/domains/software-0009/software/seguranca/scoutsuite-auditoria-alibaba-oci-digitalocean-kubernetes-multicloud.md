---
id: software.seguranca.tranche11.001018
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md", "https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditoria de Nuvens Alternativas e Clusters com Scout Suite: **Alibaba Cloud (`aliyun`), Oracle Cloud (`oci`), DigitalOcean (`do`) e Kubernetes (`k8s`)**

## Em uma frase
Muitas organizações multinacionais ou que passaram por fusões e aquisições (M&A) operam workloads fora do trio tradicional AWS/Azure/GCP — por exemplo, subsidiárias na Ásia usando **Alibaba Cloud (`aliyun`)**, bancos de dados corporativos na **Oracle Cloud Infrastructure (`oci`)**, ambientes de borda na **DigitalOcean (`do`)** ou clusters **Kubernetes (`k8s`)**.

## Por que importa
Conforme listado na documentação oficial e implementado em `ScoutSuite/providers/`, o Scout Suite permite aplicar a mesma metodologia e a mesma interface de relatório HTML para auditar todas essas plataformas!

## Como funciona
No caso de **`scout aliyun`**, você autentica com `--access-key-id` e `--access-key-secret` (auditando RAM, ECS, OSS, RDS, VPC e ActionTrail); em **`scout oci`**, ele utiliza o perfil do arquivo `~/.oci/config` (auditando Identity/IAM, Object Storage, Compute e KMS); em **`scout do`**, utiliza `--token` e chaves Spaces (`--access-key`/`--access-secret`); e em **`scout kubernetes`**, analisa o cluster via `--kubernetes-config-file` e `--kubernetes-context`!

## Exemplo
```bash
# Auditar uma conta DigitalOcean e um cluster Kubernetes especificando o contexto do kubeconfig
scout do \
  --token "${DO_READONLY_API_TOKEN}" \
  --report-dir /cases/cloud-audit/scout-digitalocean \
  --no-browser

scout kubernetes \
  --kubernetes-config-file ~/.kube/config \
  --kubernetes-context prod-cluster-admin \
  --report-dir /cases/cloud-audit/scout-k8s \
  --no-browser
```

## Limites e trade-offs
Padronizar o formato de coleta com o Scout Suite durante processos de *Due Diligence* de Segurança em M&A (Fusões e Aquisições) permite que os auditores avaliem empresas adquiridas na AWS, Azure, GCP, Alibaba Cloud, OCI ou DigitalOcean em poucas horas e entreguem relatórios comparáveis.

## Como verificar
Revise sempre se o token ou chave gerada nas nuvens avaliadas possui permissão estritamente `Read-Only` antes de iniciar a coleta.

## Conexões
- [[scoutsuite-gestao-excecoes-exceptions-json-mapeamento-ip-ranges]] — Veja também: Redução de Falsos Positivos e Enriquecimento de Rede no Scout Suite: Arquivos de Exceção (**`--exceptions`**) e Mapeamento de CIDRs Conhecidos (**`--ip-ranges`**).
- [[scoutsuite-extracao-dados-jq-automacao-cicd-defectdojo-ingestao]] — Veja também: Automação e Integração do Scout Suite em Pipelines CI/CD: Parsing do Payload JSON (`scoutsuite_results_*.js`) com **`jq`** e Ingestão no **DefectDojo**.
- [[scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup]] — Referência cruzada direta com scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup.
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Referência cruzada direta com steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud.

## Fontes
- [NCC Group Scout Suite Official GitHub — Multi-Cloud Security Auditing Tool](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md) — repositório oficial do Scout Suite cobrindo auditoria point-in-time offline para AWS, Azure, GCP, Alibaba Cloud, OCI, DigitalOcean e Kubernetes; consultado em 2026-10-03.
- [Scout Suite Official CLI & Engine Implementation (`ScoutSuite/__main__.py`)](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py) — implementação oficial dos provedores, parâmetros de autenticação, `--fetch-local`, `--update`, `--ruleset`, `--exceptions` e `--ip-ranges`; consultado em 2026-10-03.
