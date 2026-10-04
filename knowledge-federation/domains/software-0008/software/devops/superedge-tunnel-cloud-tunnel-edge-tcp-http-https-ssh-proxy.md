---
id: software.devops.tranche17.001656
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/superedge/superedge/main/README.md", "https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md", "https://github.com/superedge/superedge"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SuperEdge `tunnel-cloud` e `tunnel-edge`: tunelamento reverso TCP, HTTP, HTTPS e SSH para manutenção na borda

## Em uma frase
Os componentes `tunnel-cloud` (na nuvem) e `tunnel-edge` (nos nós de borda) mantêm conexões persistentes de saída iniciadas pela borda para permitir que o plano de controle na nuvem execute proxies de rede **TCP**, **HTTP**, **HTTPS** e **SSH** até qualquer nó de borda.

## Por que importa
Sem um túnel reverso persistente, comandos de manutenção iniciados pelo `kube-apiserver` (`kubectl logs`, `kubectl exec`, `kubectl port-forward`, coleta do `metrics-server` na porta `10250` do `kubelet`) ou sessões SSH de diagnóstico falham contra nós de borda situados atrás de NAT/firewalls.

## Como funciona
O `tunnel-edge` conecta-se ao `tunnel-cloud` e registra seu ID de nó na tabela de roteamento distribuída do túnel. Quando o `kube-apiserver` na nuvem precisa abrir uma conexão HTTPS para o `kubelet` de um nó de borda ou o operador solicita acesso SSH ao host de borda, a requisição passa pelo `tunnel-cloud`, que a encaminha pela sessão ativa do `tunnel-edge` correspondente.

## Exemplo
```bash
kubectl get pods -n edge-system -l app=tunnel-cloud
kubectl get pods -n edge-system -l app=tunnel-edge
kubectl logs -n edge-system -l app=tunnel-edge --tail=20
```

## Limites e trade-offs
Em implantações com múltiplas réplicas do `tunnel-cloud`, o componente utiliza resolução interna de DNS/cache de nós para rotear a chamada da nuvem exatamente para a instância do `tunnel-cloud` que detém a conexão TCP ativa daquele `tunnel-edge`.

## Como verificar
Execute `kubectl exec -it <pod-na-borda> -- uname -a` a partir da nuvem e valide o retorno imediato através do par `tunnel-cloud`/`tunnel-edge`.

## Conexões
- [[superedge-servicegroup-deploymentgrid-statefulsetgrid-servicegrid]] — Veja também: SuperEdge `ServiceGroup`: orquestração multi-região com `DeploymentGrid`, `StatefulSetGrid` e `ServiceGrid`.
- [[superedge-site-manager-nodeunit-nodegroup-modelagem-topologica]] — Veja também: SuperEdge `site-manager`: modelagem topológica de sites com `NodeUnit` e `NodeGroup`.

## Fontes
- [SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)](https://raw.githubusercontent.com/superedge/superedge/main/README.md) — README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm; consultado em 2026-10-03.
- [SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)](https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md) — Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3; consultado em 2026-10-03.
- [SuperEdge — Official GitHub Repository](https://github.com/superedge/superedge) — Repositório oficial Apache-2.0 do SuperEdge; consultado em 2026-10-03.
