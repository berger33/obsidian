---
id: software.devops.tranche11.001052
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
fontes: ["https://polaris.docs.fairwinds.com/infrastructure-as-code/", "https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md", "https://polaris.docs.fairwinds.com/admission-controller/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Auditoria IaC em CI/CD com o Polaris: --audit-path, --set-exit-code-on-danger, --set-exit-code-below-score e Helm charts

## Em uma frase
Na linha de comando, o comando **`polaris audit`** inspeciona diretórios de manifestos YAML (`--audit-path`) ou Helm charts (`--helm-chart` e `--helm-values`) e bloqueia pipelines de CI/CD automaticamente por meio das flags **`--set-exit-code-on-danger`** e **`--set-exit-code-below-score <0-100>`**.

## Por que importa
Gerar relatórios de segurança que ninguém lê não impede que configurações perigosas cheguem à produção. Configurar gates determinísticos no Pull Request que falham o build (`exit code != 0`) caso surja qualquer violação de nível `danger` ou caso o score de qualidade caia abaixo de um limiar (por exemplo, `90%`) força a correção antes do merge.

## Como funciona
Conforme documenta o guia *Infrastructure as Code* (`polaris.docs.fairwinds.com/infrastructure-as-code/`): (1) por padrão, `polaris audit` imprime os resultados em **JSON**, mas aceita **`--format=pretty`** (e `--color=false` para logs de CI sem suporte ANSI) para saída legível por humanos; (2) **`--only-show-failed-tests true`** filtra a saída exibindo apenas os testes que falharam; (3) **`--set-exit-code-on-danger`** faz a CLI retornar código de erro se detectar qualquer problema de severidade `danger`; (4) **`--set-exit-code-below-score 90`** falha o comando se a pontuação geral cair abaixo de 90%; e (5) **`--helm-chart ./deploy/chart --helm-values ./deploy/chart/values.yml`** audita charts Helm diretamente.

## Exemplo
```bash
# Auditar manifestos em um pipeline de CI falhando se houver qualquer item danger ou score abaixo de 90%
polaris audit --audit-path ./deploy/ \
  --format=pretty \
  --color=false \
  --only-show-failed-tests true \
  --set-exit-code-on-danger \
  --set-exit-code-below-score 90

# Auditar um Helm chart passando seu arquivo de valores
polaris audit \
  --helm-chart ./deploy/chart \
  --helm-values ./deploy/chart/values.yml \
  --set-exit-code-on-danger
```

## Limites e trade-offs
Se um repositório contiver muitos manifestos legados que já possuem avisos (`warning`), um `--set-exit-code-below-score` muito alto pode bloquear correções urgentes; uma estratégia gradual recomendada é começar com `--set-exit-code-on-danger` (bloqueando apenas falhas críticas) e elevar progressivamente o `--set-exit-code-below-score`.

## Como verificar
Execute o comando `polaris audit --audit-path ./deploy/ --set-exit-code-on-danger; echo $?` e confirme que o código de retorno é `0` para manifestos em conformidade e diferente de zero quando há um item `danger`.

## Conexões
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Veja também: Fairwinds Polaris: motor open-source de políticas para validação e remediação de configurações Kubernetes.
- [[polaris-remediacao-automatica-cli-polaris-fix-yaml]] — Veja também: Remediação automática de manifestos YAML na CLI com polaris fix --files-path e --checks.
- [[polaris-github-action-setup-polaris-automacao-pr]] — Referência cruzada direta com polaris-github-action-setup-polaris-automacao-pr.

## Fontes
- [Fairwinds Polaris Official Documentation — Infrastructure as Code (polaris audit, polaris fix, Exit Code Flags, Helm & GitHub Action)](https://polaris.docs.fairwinds.com/infrastructure-as-code/) — Guia oficial de Infrastructure as Code do Polaris cobrindo polaris audit, polaris fix, --set-exit-code-on-danger, --set-exit-code-below-score, auditoria de Helm charts e setup-polaris GitHub Action; consultado em 2026-10-03.
- [Fairwinds Polaris Official Documentation — Admission Controller & README (Validating/Mutating Webhook, 19 Default Mutations & v10.2.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md) — Documentação oficial do Admission Controller e README do Polaris detalhando Validating Webhook (danger vs warning), Mutating Webhook (--set webhook.mutate=true com 19 mutações padrão), políticas JSON Schema e imagens imutáveis v10.2.0+; consultado em 2026-10-03.
- [Fairwinds Polaris — Official Documentation & Repository](https://polaris.docs.fairwinds.com/admission-controller/) — Documentação e repositório oficial do Fairwinds Polaris; consultado em 2026-10-03.
