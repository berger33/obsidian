---
id: software.devops.tranche11.001053
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

# Remediação automática de manifestos YAML na CLI com polaris fix --files-path e --checks

## Em uma frase
O subcomando **`polaris fix --files-path <dir> --checks=all`** modifica automaticamente arquivos YAML locais de Kubernetes para corrigir problemas detectados pelas políticas do Polaris, inserindo configurações seguras e adicionando comentários onde o usuário precisa ajustar parâmetros específicos da aplicação.

## Por que importa
Quando uma equipe herda dezenas de manifestos `Deployment` sem `securityContext`, sem `requests`/`limits` e com `imagePullPolicy` incorreta, editar manualmente cada container em cada arquivo YAML é trabalhoso e propenso a erros de indentação. O `polaris fix` aplica as mutações de conformidade diretamente nos arquivos do repositório antes do commit.

## Como funciona
Conforme explica a seção *Fixing Issues* do guia oficial (`polaris.docs.fairwinds.com/infrastructure-as-code/`), ao executar `polaris fix --files-path ./deploy/ --checks=all`, a CLI analisa os manifestos YAML dentro do diretório `./deploy/` e aplica as mutações suportadas pelas regras de remediação. Para certas configurações que dependem do contexto interno da aplicação (como os caminhos ou portas exatas de `livenessProbe` e `readinessProbe`), o Polaris pode deixar comentários ao lado das alterações geradas orientando o desenvolvedor a ajustá-las para valores apropriados ao seu serviço.

## Exemplo
```bash
# Aplicar correções automáticas em todos os manifestos YAML do diretório ./deploy e inspecionar o diff no Git
polaris fix --files-path ./deploy/ --checks=all
git diff ./deploy/
```

## Limites e trade-offs
Conforme ressalta explicitamente a documentação oficial, **nem todos os problemas podem ser corrigidos automaticamente** e, atualmente, **apenas manifestos YAML puros (*raw YAML manifests*) podem sofrer mutação via `polaris fix`** — charts Helm parametrizados ainda precisam ser editados manualmente nos templates originais.

## Como verificar
Após executar `polaris fix --files-path ./deploy/ --checks=all`, rode `git diff` para revisar cada linha modificada e execute `polaris audit --audit-path ./deploy/ --format=pretty` para confirmar a elevação do score.

## Conexões
- [[polaris-auditoria-iac-cli-ci-cd-scores-danger-flags]] — Veja também: Auditoria IaC em CI/CD com o Polaris: --audit-path, --set-exit-code-on-danger, --set-exit-code-below-score e Helm charts.
- [[polaris-admission-controller-validating-mutating-webhook]] — Veja também: Polaris Admission Controller: instalação via Helm, certificados TLS (cert-manager vs caBundle) e comportamento diante de danger vs warning.
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.
- [[polaris-mutating-webhook-19-mutations-padrao]] — Referência cruzada direta com polaris-mutating-webhook-19-mutations-padrao.

## Fontes
- [Fairwinds Polaris Official Documentation — Infrastructure as Code (polaris audit, polaris fix, Exit Code Flags, Helm & GitHub Action)](https://polaris.docs.fairwinds.com/infrastructure-as-code/) — Guia oficial de Infrastructure as Code do Polaris cobrindo polaris audit, polaris fix, --set-exit-code-on-danger, --set-exit-code-below-score, auditoria de Helm charts e setup-polaris GitHub Action; consultado em 2026-10-03.
- [Fairwinds Polaris Official Documentation — Admission Controller & README (Validating/Mutating Webhook, 19 Default Mutations & v10.2.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md) — Documentação oficial do Admission Controller e README do Polaris detalhando Validating Webhook (danger vs warning), Mutating Webhook (--set webhook.mutate=true com 19 mutações padrão), políticas JSON Schema e imagens imutáveis v10.2.0+; consultado em 2026-10-03.
- [Fairwinds Polaris — Official Documentation & Repository](https://polaris.docs.fairwinds.com/admission-controller/) — Documentação e repositório oficial do Fairwinds Polaris; consultado em 2026-10-03.
