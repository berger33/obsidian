---
id: software.testes.tranche09.000302
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://kubernetes.io/docs/concepts/workloads/controllers/deployment/", "https://kubernetes.io/docs/concepts/workloads/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kubernetes Deployment: aguardar rollout e validar aplicação

## Em uma frase
Deployment reconcilia ReplicaSets e Pods até a estratégia de rollout atingir seu estado observado.

## Por que importa
Controladores Kubernetes reconciliam estado de forma assíncrona, então uma assertion instantânea sobre Pod isolado não representa necessariamente o resultado desejado. Verificar apenas spec aplicada ou Pod criado pode passar enquanto versão antiga ainda serve tráfego ou réplica não está pronta.

## Como funciona
Teste objetos e condições observáveis em cluster isolado, aguarde convergência com timeout e valide identidades e plugins que participam do comportamento. Aguarde progressão do rollout e consulte versão, disponibilidade e endpoint funcional que representa o requisito.

## Exemplo
Depois de publicar imagem nova, o teste confirma pods com digest esperado e request de smoke retorna comportamento da revisão atual.

## Limites e trade-offs
Comportamento depende da versão, controller, scheduler e plugins instalados; dry-run do API server não prova execução de rede ou workload. Condição Ready depende de probes e recursos configurados; rollout concluído não prova todas as integrações funcionais.

## Como verificar
Use `kubectl rollout status`, inspecione ReplicaSet/Pods e envie uma requisição controlada ao serviço após a convergência.

## Conexões
- [[kubernetes-cronjob-no-exactly-once]] — Veja também: Kubernetes CronJob: testar execução idempotente, não exactly-once.
- [[kubernetes-networkpolicy-plugin-enforcement-test]] — Veja também: Kubernetes NetworkPolicy: testar enforcement do plugin de rede.

## Fontes
- [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — rollout, ReplicaSets e estado observado do Deployment; consultado em 2026-10-02.
- [Kubernetes — Workloads](https://kubernetes.io/docs/concepts/workloads/) — controladores e reconciliação de workloads; consultado em 2026-10-02.
