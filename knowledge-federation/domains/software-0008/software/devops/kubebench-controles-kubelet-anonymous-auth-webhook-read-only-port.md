---
id: software.devops.tranche13.001218
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

# Aqua kube-bench: Auditoria e Endurecimento do Kubelet (Seção 4: anonymous-auth, authorization-mode e read-only-port)

## Em uma frase
Na Seção 4 (Worker Nodes) do CIS Kubernetes Benchmark executada pelo `kube-bench`, os controles críticos verificam se o `kubelet` desabilita autenticação anônima (`--anonymous-auth=false` / `authentication.anonymous.enabled: false`), exige autorização via Webhook (`authorization.mode: Webhook`) e desativa a porta somente leitura (`readOnlyPort: 0`).

## Por que importa
Um `kubelet` exposto na rede do cluster com `--anonymous-auth=true` ou com a porta `10255` (`readOnlyPort`) aberta permite que qualquer atacante com acesso de rede ao nó liste Pods ou execute comandos em containers sem passar pelo RBAC do `kube-apiserver`.

## Como funciona
O `kube-bench` inspeciona tanto os flags de linha de comando do processo `kubelet` quanto o arquivo de configuração estruturada (`--config=/var/lib/kubelet/config.yaml`), garantindo que as configurações no arquivo não sejam sobrescritas de forma insegura por argumentos de processo e que as permissões de `/var/lib/kubelet/config.yaml` sejam `600` (ou mais restritivas) e pertençam a `root:root`.

## Exemplo
```bash
# Verificar no JSON do kube-bench o resultado dos controles 4.1 e 4.2 do Kubelet:
kubectl logs job/kube-bench | grep -E "^\[(PASS|FAIL|WARN)\]\s+4\."
```

## Limites e trade-offs
Corrigir uma configuração passando uma flag na linha de comando do `kubelet` enquanto a documentação moderna do Kubernetes deprecia flags de CLI em favor do arquivo `KubeletConfiguration` (`/var/lib/kubelet/config.yaml`) cria dívida técnica para futuros upgrades.

## Como verificar
Aplique todo endurecimento do `kubelet` diretamente no objeto `KubeletConfiguration` (`/var/lib/kubelet/config.yaml`) e reexecute o `kube-bench --targets node` para confirmar `[PASS]`.

## Conexões
- [[kubebench-saida-json-junit-exit-code-automacao-ci-cronjob]] — Veja também: Aqua kube-bench: Exportação de Relatórios em JSON e JUnit (--json, --junit) e Uso em CronJobs de Auditoria.
- [[kubebench-controles-apiserver-etcd-encryption-audit-log-rbac]] — Veja também: Aqua kube-bench: Auditoria do API Server e etcd (Criptografia de Secrets, Audit Logs, TLS e Permissões PKI).

## Fontes
- [Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md) — README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição; consultado em 2026-10-03.
- [kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md) — Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões; consultado em 2026-10-03.
- [Aqua Security kube-bench — Official GitHub Repository](https://github.com/aquasecurity/kube-bench) — Repositório oficial Apache-2.0 do kube-bench; consultado em 2026-10-03.
