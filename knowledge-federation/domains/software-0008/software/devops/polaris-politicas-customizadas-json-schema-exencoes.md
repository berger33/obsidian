---
id: software.devops.tranche11.001057
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

# Políticas customizadas com JSON Schema e configuração de severidades no Fairwinds Polaris

## Em uma frase
Além das mais de 30 políticas nativas, o Polaris permite criar **políticas customizadas usando JSON Schema** diretamente no seu arquivo de configuração (`--config`), bem como calibrar a severidade (`ignore`, `warning`, `danger`) de cada checagem para alinhar a auditoria aos padrões internos da organização.

## Por que importa
Cada organização possui regras próprias que vão além das práticas gerais do Kubernetes — como exigir labels obrigatórias de centro de custo (`cost-center`, `owner`), restringir registros de imagens permitidos ou validar anotações específicas de malha de serviço. Escrever essas regras em JSON Schema padrão dispensa aprender uma linguagem proprietária complexa para validações estruturais de recursos.

## Como funciona
Conforme descreve o README oficial (`FairwindsOps/polaris`), o motor do Polaris avalia tanto as políticas embutidas quanto `customChecks` declaradas em JSON Schema. No arquivo de configuração (passado para a CLI, para o Dashboard ou para o Admission Controller via Helm values), o bloco `checks:` mapeia cada identificador de política para `ignore`, `warning` ou `danger`, enquanto `customChecks:` define esquemas JSON Schema validados contra o manifesto do workload ou container, emitindo uma mensagem customizada de `failureMessage` e categoria quando o recurso não satisfaz o schema.

## Exemplo
```yaml
# Exemplo de arquivo polaris-config.yaml ajustando severidades e declarando uma customCheck em JSON Schema
checks:
  cpuRequestsMissing: danger
  memoryLimitsMissing: danger
  pullPolicyNotAlways: ignore
   customLabelOwner: danger

customChecks:
  customLabelOwner:
    successMessage: "Label obrigatória 'owner' está presente"
    failureMessage: "Todo workload deve possuir a label 'owner'"
    category: Governance
    target: Workload
    schema:
      '$schema': http://json-schema.org/draft-07/schema
      type: object
      required: [metadata]
      properties:
        metadata:
          type: object
          required: [labels]
          properties:
            labels:
              type: object
              required: [owner]
```

## Limites e trade-offs
O JSON Schema no Polaris é excelente para validar a estrutura, presença e formato de campos dentro de um recurso individual (Workload, PodSpec ou Container), mas não realiza consultas cruzadas entre múltiplos objetos distintos da API do Kubernetes (cenário no qual motores como Kyverno ou OPA Gatekeeper são mais indicados).

## Como verificar
Execute `polaris audit --config ./polaris-config.yaml --audit-path ./deploy/ --format=pretty` para testar sua `customCheck` sobre manifestos locais antes de aplicá-la no Admission Controller.

## Conexões
- [[polaris-categorias-checagens-seguranca-eficiencia-confiabilidade]] — Veja também: Categorias de políticas embutidas do Polaris: Segurança (SecurityContext/Host), Eficiência (CPU/Memory) e Confiabilidade (Probes/Replicas/Tags).
- [[polaris-github-action-setup-polaris-automacao-pr]] — Veja também: Automação do Polaris no GitHub Actions com setup-polaris e verificação de Pull Requests.
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.
- [[polaris-auditoria-iac-cli-ci-cd-scores-danger-flags]] — Referência cruzada direta com polaris-auditoria-iac-cli-ci-cd-scores-danger-flags.

## Fontes
- [Fairwinds Polaris Official Documentation — Infrastructure as Code (polaris audit, polaris fix, Exit Code Flags, Helm & GitHub Action)](https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md) — Guia oficial de Infrastructure as Code do Polaris cobrindo polaris audit, polaris fix, --set-exit-code-on-danger, --set-exit-code-below-score, auditoria de Helm charts e setup-polaris GitHub Action; consultado em 2026-10-03.
- [Fairwinds Polaris Official Documentation — Admission Controller & README (Validating/Mutating Webhook, 19 Default Mutations & v10.2.0+ Images)](https://polaris.docs.fairwinds.com/infrastructure-as-code/) — Documentação oficial do Admission Controller e README do Polaris detalhando Validating Webhook (danger vs warning), Mutating Webhook (--set webhook.mutate=true com 19 mutações padrão), políticas JSON Schema e imagens imutáveis v10.2.0+; consultado em 2026-10-03.
- [Fairwinds Polaris — Official Documentation & Repository](https://polaris.docs.fairwinds.com/admission-controller/) — Documentação e repositório oficial do Fairwinds Polaris; consultado em 2026-10-03.
