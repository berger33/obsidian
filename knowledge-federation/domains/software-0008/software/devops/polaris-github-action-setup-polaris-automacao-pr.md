---
id: software.devops.tranche11.001058
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

# Automação do Polaris no GitHub Actions com setup-polaris e verificação de Pull Requests

## Em uma frase
O repositório oficial do Polaris disponibiliza a GitHub Action **`fairwindsops/polaris/.github/actions/setup-polaris`** para baixar uma versão específica do binário `polaris`, adicioná-la ao `PATH` do runner e executar auditorias de *policy-as-code* diretamente nos jobs de integração contínua.

## Por que importa
Integrar o Polaris diretamente no workflow de Pull Request do GitHub garante feedback rápido ao desenvolvedor quando ele altera um manifesto Kubernetes ou Helm chart, barrando violações de segurança e eficiência antes que o código chegue à branch principal e ao controlador GitOps.

## Como funciona
Conforme documentado na seção *As Github Action / Setup polaris action* (`polaris.docs.fairwinds.com/infrastructure-as-code/`), a action `fairwindsops/polaris/.github/actions/setup-polaris@master` recebe o input `version` (no formato `<tag_name>`, determinando qual release baixar) e expõe o output `version`. Uma vez executada a etapa de setup, os passos seguintes do mesmo job no GitHub Actions podem invocar diretamente `polaris version`, `polaris audit` ou `polaris fix`.

## Exemplo
```yaml
# Workflow do GitHub Actions instalando o Polaris e auditando os manifestos do diretório ./deploy
name: Polaris IaC Audit
on: [pull_request]
jobs:
  polaris-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup polaris
        uses: fairwindsops/polaris/.github/actions/setup-polaris@master
        with:
          version: v10.2.0
      - name: Run Polaris Audit
        run: |
          polaris audit --audit-path ./deploy/ \
            --format=pretty \
            --only-show-failed-tests true \
            --set-exit-code-on-danger \
            --set-exit-code-below-score 85
```

## Limites e trade-offs
Sempre fixe uma tag explícita no input `version` compatível com as regras do seu arquivo `polaris-config.yaml`, garantindo que todos os desenvolvedores localmente e o runner de CI avaliem exatamente o mesmo conjunto de políticas embutidas.

## Como verificar
Inspecione os logs do job no GitHub Actions confirmando a saída de `polaris version` e o resultado da etapa `polaris audit`.

## Conexões
- [[polaris-politicas-customizadas-json-schema-exencoes]] — Veja também: Políticas customizadas com JSON Schema e configuração de severidades no Fairwinds Polaris.
- [[polaris-migracao-registro-imagens-assinadas-imutaveis-v10-2]] — Veja também: Migração de registro e imagens imutáveis assinadas no Fairwinds Polaris (v10.2.0+).
- [[polaris-auditoria-iac-cli-ci-cd-scores-danger-flags]] — Referência cruzada direta com polaris-auditoria-iac-cli-ci-cd-scores-danger-flags.
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.
- [[pluto-integracao-github-action-ci-cd-detect-files]] — Referência cruzada direta com pluto-integracao-github-action-ci-cd-detect-files.

## Fontes
- [Fairwinds Polaris Official Documentation — Infrastructure as Code (polaris audit, polaris fix, Exit Code Flags, Helm & GitHub Action)](https://polaris.docs.fairwinds.com/infrastructure-as-code/) — Guia oficial de Infrastructure as Code do Polaris cobrindo polaris audit, polaris fix, --set-exit-code-on-danger, --set-exit-code-below-score, auditoria de Helm charts e setup-polaris GitHub Action; consultado em 2026-10-03.
- [Fairwinds Polaris Official Documentation — Admission Controller & README (Validating/Mutating Webhook, 19 Default Mutations & v10.2.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md) — Documentação oficial do Admission Controller e README do Polaris detalhando Validating Webhook (danger vs warning), Mutating Webhook (--set webhook.mutate=true com 19 mutações padrão), políticas JSON Schema e imagens imutáveis v10.2.0+; consultado em 2026-10-03.
- [Fairwinds Polaris — Official Documentation & Repository](https://polaris.docs.fairwinds.com/admission-controller/) — Documentação e repositório oficial do Fairwinds Polaris; consultado em 2026-10-03.
