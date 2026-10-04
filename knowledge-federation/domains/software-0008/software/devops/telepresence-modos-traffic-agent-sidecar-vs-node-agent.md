---
id: software.devops.tranche09.000884
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md", "https://telepresence.io/docs/concepts/architecture", "https://github.com/telepresenceio/telepresence"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Telepresence: escolha entre Traffic Agent como Sidecar injetado (padrão) ou Node-Agent sem reiniciar pods

## Em uma frase
O `Traffic Agent` do Telepresence pode operar de duas maneiras configuráveis no cluster: injetado como um container **sidecar** no pod alvo (o padrão) ou executando como um **node-agent** (um pod hospedado no nó que se anexa aos namespaces do workload sem modificá-lo e sem reiniciar o pod).

## Por que importa
Na abordagem clássica de sidecar, na primeira vez que um desenvolvedor faz `intercept` em um Deployment, o webhook do `Traffic Manager` precisa injetar o container `traffic-agent` no pod template, o que força o Kubernetes a recriar/reiniciar o pod (podendo ser bloqueado por políticas estritas de admissão ou interromper estados em memória). O README oficial e a página `Architecture` (v2.32) destacam o novo modo **node-agent**.

## Como funciona
Conforme documenta a seção `Traffic Agent` em `telepresence.io/docs/concepts/architecture`: (1) **Sidecar (padrão)**: na primeira anexação (`replace`, `ingest`, `intercept` ou `wiretap`), o `Traffic Manager` usa um Mutating Admission Webhook para injetar o container sidecar `traffic-agent` dentro do(s) pod(s) do workload, redirecionando as portas no namespace de rede do pod sem exigir privilégios em nível de nó; e (2) **Node-hosted agent (`node-agent`)**: um administrador do cluster pode configurar o Helm chart do Telepresence para rodar o `traffic-agent` como um pod hospedado no nó (DaemonSet/node-agent) que se anexa diretamente aos namespaces dos pods existentes no nó **sem injetar sidecar, sem alterar a especificação do Deployment e sem reiniciar o pod**.

## Exemplo
```bash
# Verificar o status do Traffic Agent nos workloads anexados usando telepresence list ou kubectl describe pod
telepresence list
kubectl describe pod -l app=checkout-service | grep -A 5 "traffic-agent"
```

## Limites e trade-offs
O modo **sidecar** padrão não exige privilégios elevados de host nos nós workers (rodando dentro do próprio contexto de segurança do pod), mas causa o rollout inicial do pod ao injetar o sidecar (que pode ser removido depois com `telepresence uninstall <workload>`); já o modo **node-agent** evita completamente qualquer modificação ou restart nos pods da aplicação, mas exige que o pod do `node-agent` no nó worker tenha permissões privilegiadas no host para entrar nos namespaces de rede dos containers locais.

## Como verificar
Consulte `telepresence list` e `kubectl get pods` durante uma sessão de `intercept` para verificar se o cluster está operando com injeção de sidecar (`2/2 Ready`) ou via `node-agent` (`1/1 Ready`).

## Conexões
- [[telepresence-filtragem-trafego-http-headers-paths-equipes]] — Veja também: Telepresence: interceptações seletivas por cabeçalho HTTP (--http-header) e caminho (--http-path-*) em clusters compartilhados.
- [[telepresence-ambiente-remoto-variaveis-montagem-volumes-locais]] — Veja também: Telepresence: importação de variáveis de ambiente (--env-file) e montagem de volumes remotos (--mount) no processo local.
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Referência cruzada direta com telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura.
- [[telepresence-quatro-modos-anexacao-replace-intercept-wiretap-ingest]] — Referência cruzada direta com telepresence-quatro-modos-anexacao-replace-intercept-wiretap-ingest.
- [[mirrord-arquitetura-mirrord-layer-mirrord-agent-capabilities]] — Referência cruzada direta com mirrord-arquitetura-mirrord-layer-mirrord-agent-capabilities.

## Fontes
- [Telepresence GitHub — README.md (CNCF Local-to-Cluster Development, 4 Attachment Modes & Traffic Filtering)](https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md) — README oficial do Telepresence (v2) detalhando eliminação do ciclo build/push/deploy, modos replace/intercept/wiretap/ingest, filtragem HTTP para equipes e importação de ambiente/volumes; consultado em 2026-10-03.
- [Telepresence Official Documentation — Architecture (User-Daemon, Root-Daemon VIF, Traffic Manager & Sidecar vs Node-Agent)](https://telepresence.io/docs/concepts/architecture) — Documentação oficial de arquitetura do Telepresence v2.32 explicando User-Daemon, Root-Daemon (Virtual Network Device VIF), Traffic Manager (telepresence helm install) e Traffic Agent como sidecar ou node-agent sem restart; consultado em 2026-10-03.
- [Telepresence — Official GitHub Repository](https://github.com/telepresenceio/telepresence) — Repositório oficial Apache-2.0 do Telepresence na CNCF; consultado em 2026-10-03.
