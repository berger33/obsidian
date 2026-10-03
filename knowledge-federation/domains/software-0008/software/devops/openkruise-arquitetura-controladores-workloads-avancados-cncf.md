---
id: software.devops.tranche16.001551
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/openkruise/kruise/master/README.md", "https://openkruise.io/docs/user-manuals/cloneset/", "https://github.com/openkruise/kruise"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenKruise: suíte CNCF de controladores avançados de workloads e atualizações in-place no Kubernetes

## Em uma frase
O OpenKruise (projeto CNCF Incubating, escrito em Go) é uma suíte de controladores e webhooks que estende e complementa os controladores nativos do Kubernetes (`Deployment`, `StatefulSet`, `DaemonSet`, `Job`, `CronJob`) com atualizações *in-place*, orquestração de sidecars, distribuição multi-domínio e proteção contra deleção em cascata.

## Por que importa
Os controladores core do Kubernetes recriam o Pod inteiro (gerando novo IP, novo agendamento e remontagem de volumes) até mesmo quando apenas a tag de imagem de um container mudou, o que causa alto custo de inicialização e perda de cache de memória ou estado local em clusters de grande escala.

## Como funciona
Instalado via Helm (`kruise-manager` e `kruise-daemon`), o OpenKruise registra Custom Resource Definitions no grupo `apps.kruise.io` e `policy.kruise.io`. Seus controladores gerenciam Pods diretamente (padrão sufixo `-Set`), coordenando com o daemon de nó (`kruise-daemon`) para reiniciar containers individualmente via CRI sem destruir o Pod sandbox nem alterar o endereço IP.

## Exemplo
```bash
helm repo add openkruise https://openkruise.github.io/charts/
helm upgrade --install kruise openkruise/kruise --version 1.8.0 --namespace kruise-system --create-namespace
kubectl get pods -n kruise-system
```

## Limites e trade-offs
Como o OpenKruise utiliza mutating e validating admission webhooks para injetar metadados de atualização in-place e proteger recursos, a indisponibilidade de todos os pods do `kruise-controller-manager` pode bloquear a criação de novos Pods caso as políticas de falha não estejam dimensionadas em alta disponibilidade.

## Como verificar
Verifique que os Pods `kruise-controller-manager` (em múltiplas réplicas com leader election) e o DaemonSet `kruise-daemon` estão `Running` e `Ready` no namespace `kruise-system`.

## Conexões
- [[openkruise-cloneset-in-place-update-preservacao-ip-sandbox]] — Veja também: OpenKruise CloneSet: atualização in-place de containers (`InPlaceIfPossible`) preservando IP e Pod sandbox.

## Fontes
- [OpenKruise GitHub — README.md (Advanced Workloads, In-Place Update, Sidecar Management, Multi-Domain & Application Protection)](https://raw.githubusercontent.com/openkruise/kruise/master/README.md) — README oficial do openkruise/kruise (CNCF Incubating) listando os controladores avançados de workload, operações aprimoradas e proteções de disponibilidade; consultado em 2026-10-03.
- [OpenKruise Official Documentation — CloneSet User Manual (Scale Features, PVC Templates, disablePVCReuse & Selective Pod Deletion)](https://openkruise.io/docs/user-manuals/cloneset/) — Manual oficial do CloneSet no OpenKruise detalhando suporte a PVCs, atualização in-place, podsToDelete e sequência de prioridades de deleção; consultado em 2026-10-03.
- [OpenKruise — Official GitHub Repository](https://github.com/openkruise/kruise) — Repositório oficial Apache-2.0 do OpenKruise na CNCF; consultado em 2026-10-03.
