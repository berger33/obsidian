---
id: software.devops.tranche13.001212
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md", "https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md", "https://github.com/aquasecurity/kube-bench"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Aqua kube-bench: Autodetecção de Versão do Kubernetes e Mapeamento para Releases do CIS Benchmark

## Em uma frase
Por padrão, o `kube-bench` detecta automaticamente a versão do Kubernetes em execução no nó (consultando o binário `kubelet` ou `kubectl` disponível no `PATH`) e os componentes ativos na máquina para selecionar a suíte correspondente do CIS Kubernetes Benchmark.

## Por que importa
Não existe um mapeamento um-para-um entre cada release do Kubernetes e uma release do CIS Benchmark (já que o CIS publica revisões em cadência diferente das releases trimestrais do Kubernetes), o que causa dúvidas sobre qual `--benchmark` ou `--version` aplicar.

## Como funciona
Quando executado em container (`docker run --pid=host`), montar o binário `kubectl` ou `kubelet` do host (`-v $(which kubectl):/usr/local/mount-from-host/bin/kubectl`) e o `KUBECONFIG` permite que o `kube-bench` descubra a versão do cluster automaticamente, ou o operador pode forçar explicitamente a versão alvo via flag `--version` ou `--benchmark`.

## Exemplo
```bash
docker run --rm --pid=host \
  -v /etc:/etc:ro \
  -v /var:/var:ro \
  -v "$(which kubectl):/usr/local/mount-from-host/bin/kubectl:ro" \
  -v ~/.kube:/.kube:ro \
  -e KUBECONFIG=/.kube/config \
  docker.io/aquasec/kube-bench:latest
```

## Limites e trade-offs
Executar a imagem Docker do `kube-bench` sem montar `kubectl`/`kubelet` e sem passar `--version` ou `--benchmark` faz a autodetecção de versão falhar quando o container isolado não consegue consultar o servidor da API.

## Como verificar
Explicite `--benchmark` (por exemplo, `cis-1.8`, `eks-1.5.0`, `gke-1.6.0`) ou monte o binário `kubectl` e o `KUBECONFIG` para autodetecção determinística.

## Conexões
- [[kubebench-auditoria-cis-kubernetes-benchmark-arquitetura-yaml]] — Veja também: Aqua kube-bench: Auditoria de Segurança com CIS Kubernetes Benchmark Baseada em YAML.
- [[kubebench-control-plane-master-nodes-nodeselector-tolerations]] — Veja também: Aqua kube-bench: Execução de Controles de Control Plane (Master, API Server, etcd, Scheduler) com Tolerations.

## Fontes
- [Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md) — README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição; consultado em 2026-10-03.
- [kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md) — Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões; consultado em 2026-10-03.
- [Aqua Security kube-bench — Official GitHub Repository](https://github.com/aquasecurity/kube-bench) — Repositório oficial Apache-2.0 do kube-bench; consultado em 2026-10-03.
