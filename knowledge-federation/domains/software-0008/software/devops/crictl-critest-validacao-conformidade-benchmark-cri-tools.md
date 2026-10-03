---
id: software.devops.tranche14.001400
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md", "https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md", "https://github.com/kubernetes-sigs/cri-tools"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# crictl & critest: Suíte Oficial de Conformidade e Benchmark de Performance para Runtimes CRI

## Em uma frase
Além da CLI `crictl`, o repositório `kubernetes-sigs/cri-tools` fornece o **`critest`**, a suíte oficial de testes de validação de conformidade e benchmark de performance para qualquer implementação da **Kubelet Container Runtime Interface (CRI)**.

## Por que importa
Ao qualificar uma nova versão do `containerd`, `CRI-O` ou um runtime alternativo em uma imagem de sistema operacional de nó (Node OS), é necessário comprovar que o runtime atende 100% do contrato CRI exigido por aquela versão do Kubernetes.

## Como funciona
O binário `critest` conecta-se ao `--runtime-endpoint` e executa automaticamente os testes funcionais de conformidade (`critest --validation`) ou os testes de benchmark de ciclo de vida de Pods e containers (`critest --benchmark`), verificando criação de sandboxes, streaming, port-forward, security contexts e limpeza.

## Exemplo
```bash
critest --version
sudo critest --runtime-endpoint=unix:///run/containerd/containerd.sock --parallel=4
```

## Limites e trade-offs
Executar a suíte `critest` diretamente em um worker node ativo que já está rodando cargas de trabalho de produção cria e destrói dezenas de PodSandboxes de teste e pode interferir no ambiente.

## Como verificar
Execute o `critest` exclusivamente em nós de homologação, pipelines de CI de construção de imagens de nós (AMI/OVA) ou antes de ingressar o nó no cluster de produção.

## Conexões
- [[crictl-execucao-sandboxes-containers-json-yaml-runp-create-start]] — Veja também: crictl: Teste Isolado de Runtimes CRI sem Kubelet usando Arquivos JSON/YAML (runp, create, start e run).

## Fontes
- [cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md) — Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout; consultado em 2026-10-03.
- [kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md) — README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes; consultado em 2026-10-03.
- [Kubernetes SIG Node cri-tools — Official GitHub Repository](https://github.com/kubernetes-sigs/cri-tools) — Repositório oficial Apache-2.0 do cri-tools; consultado em 2026-10-03.
