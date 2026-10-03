---
id: software.seguranca.tranche02.000175
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://docs.prowler.com/introduction", "https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md", "https://github.com/prowler-cloud/prowler"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Prowler `Mutelist` (`-w` / `--mutelist-file`): gerenciamento declarativo de exceções por conta, região, check, recurso e tags

## Em uma frase
O recurso **Mutelist (`-w` / `--mutelist-file mutelist.yaml`)** do Prowler permite silenciar (*status `MUTED`*) achados específicos que são exceções arquiteturais conhecidas e aprovadas, combinando expressões regulares ou wildcards (`*`) sobre **`Accounts`**, **`Regions`**, **`Checks`**, **`Resources`** e **`Tags`** (além de `Exceptions` para desmutar subcasos).

## Por que importa
Em toda organização existem buckets S3 intencionalmente públicos (por exemplo, o bucket de assets estáticos do site institucional) ou contas de sandbox; se esses recursos gerarem alertas `FAIL` críticos todos os dias, a equipe sofrerá fadiga de alertas.

## Como funciona
Diferente de excluir o check inteiro (`--excluded-checks`), a `mutelist.yaml` preserva a rastreabilidade de auditoria: o check continua sendo executado e registrado no relatório como `MUTED` (não falhando o código de saída do Prowler por padrão), e você pode hospedar o arquivo `mutelist.yaml` centralmente em um bucket S3 (`-w s3://meu-bucket-sec/mutelist.yaml`) ou DynamoDB!

## Exemplo
```yaml
Mutelist:
  Accounts:
    "123456789012":
      Checks:
        s3_bucket_public_access:
          Regions:
            - "us-east-1"
            - "sa-east-1"
          Resources:
            - "corp-public-website-assets-*"
          Tags:
            - "PublicWebsite=true"
          Description: "Bucket público aprovado pelo comitê de arquitetura para CDN estática."
```

## Limites e trade-offs
Exija que toda entrada na `mutelist.yaml` restrinja simultaneamente `Checks` e `Resources` (ou `Tags`) e preencha o campo `Description` com o número do ticket de aprovação de risco.

## Como verificar
Execute `prowler aws -w ./mutelist.yaml -c s3_bucket_public_access` e confirme que os recursos listados aparecem como `MUTED`.

## Conexões
- [[prowler-selecao-granular-checks-services-severities-categories-regions]] — Veja também: Prowler Filtragem Granular de Execução: `--checks`, `--services`, `--severity`, `--category` e `--region` / `--excluded-checks`.
- [[prowler-auditoria-kubernetes-clusters-kubeconfig-in-cluster-rbac-pss]] — Veja também: Prowler para Kubernetes (`prowler kubernetes`): auditoria CIS Kubernetes Benchmark, RBAC, Pod Security e NetworkPolicies.

## Fontes
- [Prowler GitHub — README.md (Open-Source Cloud Security Platform, CLI/Dashboard/Server Architecture, Attack Paths with Cartography/Neo4j & Security Hub)](https://docs.prowler.com/introduction) — README oficial do prowler-cloud/prowler documentando a arquitetura da plataforma, execução multi-cloud, configuração de Attack Paths com Neo4j/Amazon Neptune e formatos de saída; consultado em 2026-10-03.
- [Prowler Official Documentation — Introduction & Supported Providers (AWS/Azure/GCP/Kubernetes/SaaS/IaC Coverage, ThreatScore, Compliance & Prowler MCP)](https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md) — Documentação oficial de introdução ao Prowler detalhando a matriz de provedores suportados, Prowler ThreatScore, frameworks de conformidade, Mutelist e extensibilidade; consultado em 2026-10-03.
- [Prowler — Official GitHub Repository](https://github.com/prowler-cloud/prowler) — Repositório oficial Apache-2.0 do Prowler; consultado em 2026-10-03.
