---
id: software.devops.tranche11.001083
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
fontes: ["https://kubevela.io/docs/quick-start/", "https://raw.githubusercontent.com/kubevela/kubevela/master/README.md", "https://kubevela.io/docs/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Operação de Workflows e CLI do KubeVela: vela up, status, workflowSuspending, workflow resume, port-forward, exec e logs

## Em uma frase
A CLI **`vela`** gerencia todo o ciclo de vida operacional de uma `Application` — desde o deploy (`vela up -f`), inspeção de saúde e endpoints (`vela status`), acesso direto (`vela port-forward`, `vela exec`, `vela logs`), até a aprovação manual de workflows pausados (`workflowSuspending` → `vela workflow resume`) e remoção (`vela delete`).

## Por que importa
Ao promover uma nova versão entre `default` (teste/staging) e `prod`, a equipe precisa validar o serviço no primeiro ambiente, inspecionar seus logs e testar o endpoint HTTP antes de autorizar o rollout em produção com alta disponibilidade (`replicas: 2`). O passo `type: suspend` combinado com a CLI `vela` torna esse gate nativo no controlador.

## Como funciona
Conforme o passo a passo do guia *Deploy First Application* (`kubevela.io/docs/quick-start/`): (1) após executar `vela up -f first-app.yaml`, o KubeVela executa o primeiro passo (`deploy2default`), implanta o `webservice` no namespace `default` com `1/1` réplica pronta e pausa no segundo passo (`type: suspend`), mudando o status da Application para **`workflowSuspending`**; (2) o engenheiro valida a instância em staging usando `vela port-forward first-vela-app 8000:8000`, `vela logs first-vela-app` ou `vela exec first-vela-app`; (3) uma vez validada, executa **`vela workflow resume first-vela-app`**, fazendo o controlador avançar para o passo `deploy2prod`, que aplica as políticas `target-prod` e `deploy-ha` (`Ready: 2/2` no namespace `prod`) e muda o status da Application para **`running`**; e (4) `vela delete first-vela-app` limpa a aplicação.

## Exemplo
```bash
# Inspecionar a aplicação pausada em aprovação manual, testar via port-forward e aprovar a continuação para produção
vela status first-vela-app
vela port-forward first-vela-app 8000:8000
vela workflow resume first-vela-app
vela status first-vela-app --endpoint
```

## Limites e trade-offs
Enquanto a aplicação estiver no estado `workflowSuspending` aguardando `vela workflow resume`, as alterações subsequentes nos passos seguintes do workflow (`deploy2prod`) permanecem retidas até que o operador retome explicitamente ou reinicie/aborte o workflow.

## Como verificar
Execute `vela status first-vela-app` antes e depois de `vela workflow resume first-vela-app`, confirmando a transição de `Status: workflowSuspending` (apenas `default` com `Ready:1/1`) para `Status: running` (`prod` com `Ready:2/2` e `default` com `Ready:1/1`).

## Conexões
- [[kubevela-anatomia-crd-application-components-traits-policies-workflow]] — Veja também: Anatomia do recurso Application (core.oam.dev/v1beta1) no KubeVela: Components, Traits, Policies e Workflow.
- [[kubevela-console-velaux-sincronizacao-fonte-verdade-gitops]] — Veja também: Console UI VelaUX vs CLI/GitOps no KubeVela: arquitetura de metadados e regra de fonte única da verdade.
- [[kubevela-plataforma-entrega-aplicacoes-oam-cue-cncf]] — Referência cruzada direta com kubevela-plataforma-entrega-aplicacoes-oam-cue-cncf.

## Fontes
- [KubeVela GitHub — README.md & Introduction Docs (Deployment as Code, OAM, CUE, 0.5c1g Control Plane & Comparison Matrix)](https://kubevela.io/docs/quick-start/) — README oficial e introdução da documentação do KubeVela (v1.11) detalhando Open Application Model (OAM), extensibilidade com CUE, footprint de control plane (1 pod 0.5c1g) e comparação com CI/CD, GitOps, PaaS e Helm; consultado em 2026-10-03.
- [KubeVela Official Documentation — Deploy First Application Quick Start (Application CRD, Components, Traits, Policies, Workflow Suspend/Resume & VelaUX)](https://raw.githubusercontent.com/kubevela/kubevela/master/README.md) — Guia prático oficial Quick Start do KubeVela demonstrando a estrutura da CRD Application (core.oam.dev/v1beta1), políticas topology e override, workflow com suspend/resume na CLI vela e regra de sincronização com o console VelaUX; consultado em 2026-10-03.
- [KubeVela — Official Documentation & Repository](https://kubevela.io/docs/) — Documentação e repositório oficial do KubeVela; consultado em 2026-10-03.
