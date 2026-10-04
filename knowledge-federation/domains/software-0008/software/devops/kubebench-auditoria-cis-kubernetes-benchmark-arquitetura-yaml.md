---
id: software.devops.tranche13.001211
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
fontes: ["https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md", "https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md", "https://github.com/aquasecurity/kube-bench"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Aqua kube-bench: Auditoria de Segurança com CIS Kubernetes Benchmark Baseada em YAML

## Em uma frase
O `kube-bench` (desenvolvido pela Aqua Security sob licença Apache-2.0) é uma ferramenta em Go que verifica se um cluster Kubernetes está implantado de forma segura executando os controles documentados no **CIS Kubernetes Benchmark** definidos em arquivos de configuração YAML modulares.

## Por que importa
Auditar manualmente dezenas de flags de inicialização do `kube-apiserver`, `etcd`, `kube-controller-manager`, `kube-scheduler` e `kubelet`, além de permissões `chmod`/`chown` de arquivos de certificado e `kubeconfig` em cada nó, é inviável e sujeito a erro humano.

## Como funciona
O `kube-bench` inspeciona os processos em execução no nó (via namespace de PID do host) e os arquivos de configuração em `/etc` e `/var`, avaliando cada controle (`[PASS]`, `[FAIL]`, `[WARN]`, `[INFO]`) contra as especificações YAML de cada versão do benchmark em `/opt/kube-bench/cfg/`. Além do uso standalone ou via Job, ele também integra a varredura CIS do Trivy CLI e do Trivy Operator.

## Exemplo
```bash
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job.yaml
kubectl get pods -l app=kube-bench
kubectl logs -l app=kube-bench
```

## Limites e trade-offs
Executar o `kube-bench` dentro de um container ou Pod sem compartilhar o namespace de PID do host (`hostPID: true` / `--pid=host`) faz com que a ferramenta não enxergue os processos `kube-apiserver` ou `kubelet` em execução no nó.

## Como verificar
Garanta que o Job ou container do `kube-bench` rode com `hostPID: true` e montagens somente leitura (`ro`) dos diretórios `/etc` e `/var` do host.

## Conexões
- [[kubebench-autodetect-versao-kubernetes-mapeamento-cis-benchmark]] — Veja também: Aqua kube-bench: Autodetecção de Versão do Kubernetes e Mapeamento para Releases do CIS Benchmark.

## Fontes
- [Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md) — README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição; consultado em 2026-10-03.
- [kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md) — Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões; consultado em 2026-10-03.
- [Aqua Security kube-bench — Official GitHub Repository](https://github.com/aquasecurity/kube-bench) — Repositório oficial Apache-2.0 do kube-bench; consultado em 2026-10-03.
