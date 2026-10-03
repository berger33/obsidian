---
id: software.devops.tranche11.001051
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
fontes: ["https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md", "https://polaris.docs.fairwinds.com/infrastructure-as-code/", "https://polaris.docs.fairwinds.com/admission-controller/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds Polaris: motor open-source de políticas para validação e remediação de configurações Kubernetes

## Em uma frase
O Fairwinds Polaris (`FairwindsOps/polaris`, Apache-2.0) é um motor open-source de políticas para Kubernetes que valida e remedia configurações de workloads, oferecendo mais de **30 políticas embutidas** de boas práticas, suporte a políticas customizadas com **JSON Schema** e operação em três modos: **Dashboard**, **Admission Controller** (validating/mutating webhook) e **CLI** para CI/CD.

## Por que importa
Pequenos descuidos em manifestos YAML do Kubernetes — como esquecer `readinessProbe`, rodar containers como `root`, permitir escalação de privilégios (`allowPrivilegeEscalation`), usar a tag `:latest` ou omitir limites de memória — causam incidentes de estabilidade e brechas de segurança em produção. O Polaris aplica as mesmas regras de *policy-as-code* desde o repositório Git até o webhook de admissão do cluster.

## Como funciona
Conforme descrevem o README oficial (`FairwindsOps/polaris`) e a página inicial da documentação (`polaris.docs.fairwinds.com`), a arquitetura do Polaris permite executar exatamente o mesmo conjunto de checagens em três estágios: (1) **Command-line tool (`polaris audit` / `polaris fix`)**: audita e corrige arquivos YAML locais ou Helm charts durante o pipeline de CI/CD; (2) **Admission Controller**: atua como Validating Webhook (rejeitando workloads que violem políticas de severidade `danger`) ou Mutating Webhook (modificando automaticamente o pod spec na admissão); e (3) **Dashboard**: interface web que escaneia o cluster em execução e calcula um score percentual de conformidade por namespace e por workload.

## Exemplo
```bash
# Instalar a CLI do Polaris via Homebrew e auditar um diretório local de manifestos Kubernetes
brew tap FairwindsOps/tap
brew install FairwindsOps/tap/polaris
polaris version
polaris audit --audit-path ./deploy/ --format=pretty
```

## Limites e trade-offs
Quando executado sobre arquivos locais, o Polaris avalia manifestos YAML renderizados; para auditar templates Helm parametrizados, é necessário passar `--helm-chart` e `--helm-values` (ou renderizar previamente com `helm template`), e a mutação automática (`polaris fix`) altera apenas arquivos YAML puros, não templates Helm cheios de diretivas Go `{{ ... }}`.

## Como verificar
Execute `polaris audit --audit-path ./deploy/ --format=pretty` e verifique o score geral calculado e a contagem de checagens aprovadas, `warning` e `danger`.

## Conexões
- [[polaris-auditoria-iac-cli-ci-cd-scores-danger-flags]] — Veja também: Auditoria IaC em CI/CD com o Polaris: --audit-path, --set-exit-code-on-danger, --set-exit-code-below-score e Helm charts.
- [[polaris-remediacao-automatica-cli-polaris-fix-yaml]] — Referência cruzada direta com polaris-remediacao-automatica-cli-polaris-fix-yaml.
- [[polaris-admission-controller-validating-mutating-webhook]] — Referência cruzada direta com polaris-admission-controller-validating-mutating-webhook.

## Fontes
- [Fairwinds Polaris Official Documentation — Infrastructure as Code (polaris audit, polaris fix, Exit Code Flags, Helm & GitHub Action)](https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md) — Guia oficial de Infrastructure as Code do Polaris cobrindo polaris audit, polaris fix, --set-exit-code-on-danger, --set-exit-code-below-score, auditoria de Helm charts e setup-polaris GitHub Action; consultado em 2026-10-03.
- [Fairwinds Polaris Official Documentation — Admission Controller & README (Validating/Mutating Webhook, 19 Default Mutations & v10.2.0+ Images)](https://polaris.docs.fairwinds.com/infrastructure-as-code/) — Documentação oficial do Admission Controller e README do Polaris detalhando Validating Webhook (danger vs warning), Mutating Webhook (--set webhook.mutate=true com 19 mutações padrão), políticas JSON Schema e imagens imutáveis v10.2.0+; consultado em 2026-10-03.
- [Fairwinds Polaris — Official Documentation & Repository](https://polaris.docs.fairwinds.com/admission-controller/) — Documentação e repositório oficial do Fairwinds Polaris; consultado em 2026-10-03.
