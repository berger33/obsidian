---
id: software.devops.tranche14.001399
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md", "https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md", "https://github.com/kubernetes-sigs/cri-tools"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# crictl: Teste Isolado de Runtimes CRI sem Kubelet usando Arquivos JSON/YAML (runp, create, start e run)

## Em uma frase
Para desenvolvedores e engenheiros de plataforma que precisam validar um runtime CRI (`containerd`, `CRI-O`, `Kata Containers` ou `gVisor`) antes mesmo de iniciar o `kubelet`, o `crictl` permite criar PodSandboxes e containers a partir de arquivos de configuração JSON ou YAML usando `crictl runp`, `crictl create`, `crictl start` e `crictl run`.

## Por que importa
Quando um runtime de isolamento (como Kata Containers ou gVisor) falha ao iniciar um Pod no Kubernetes, testar o runtime isoladamente com um arquivo `pod-config.json` e `container-config.json` separa problemas do `kubelet` de problemas do runtime/CNI.

## Como funciona
Executando `POD_ID=$(crictl runp pod-config.json)`, o runtime cria o PodSandbox e configura a rede CNI; em seguida, `CONTAINER_ID=$(crictl create $POD_ID container-config.json pod-config.json)` e `crictl start $CONTAINER_ID` iniciam o container (ou faz-se tudo em um passo com `crictl run container-config.json pod-config.json`), limpando depois com `crictl stopp` e `crictl rmp`.

## Exemplo
```bash
POD_ID=$(crictl runp pod-config.json)
CONTAINER_ID=$(crictl create "$POD_ID" container-config.json pod-config.json)
crictl start "$CONTAINER_ID"
crictl ps
crictl stopp "$POD_ID" && crictl rmp "$POD_ID"
```

## Limites e trade-offs
Esquecer de executar `crictl pull <imagem>` antes de rodar `crictl create` quando `pull-image-on-create: false` (padrão no `/etc/crictl.yaml`) faz o `crictl create` falhar se a imagem ainda não estiver no cache local.

## Como verificar
Baixe a imagem explicitamente com `crictl pull` antes de executar `crictl create` (ou use `crictl run`, que faz o pull automaticamente a menos que `--no-pull` seja passado).

## Conexões
- [[crictl-update-limites-cgroup-cpu-memory-containers-vivos]] — Veja também: crictl: Atualização Dinâmica de Limites de Cgroup (crictl update) e Tracing OpenTelemetry.
- [[crictl-critest-validacao-conformidade-benchmark-cri-tools]] — Veja também: crictl & critest: Suíte Oficial de Conformidade e Benchmark de Performance para Runtimes CRI.

## Fontes
- [cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md) — Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout; consultado em 2026-10-03.
- [kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md) — README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes; consultado em 2026-10-03.
- [Kubernetes SIG Node cri-tools — Official GitHub Repository](https://github.com/kubernetes-sigs/cri-tools) — Repositório oficial Apache-2.0 do cri-tools; consultado em 2026-10-03.
