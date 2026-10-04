---
id: software.devops.tranche13.001219
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

# Aqua kube-bench: Auditoria do API Server e etcd (Criptografia de Secrets, Audit Logs, TLS e Permissões PKI)

## Em uma frase
Nas Seções 1 e 2 do CIS Kubernetes Benchmark verificadas pelo `kube-bench` nos nós de control plane, a ferramenta audita a segurança dos manifestos estáticos em `/etc/kubernetes/manifests/`, as permissões `600`/`700` dos certificados em `/etc/kubernetes/pki/` e flags críticas como `--encryption-provider-config`, `--audit-log-path`, `--authorization-mode=Node,RBAC` e mTLS do `etcd` (`--client-cert-auth=true`, `--peer-client-cert-auth=true`).

## Por que importa
Em clusters provisionados com `kubeadm` ou ferramentas on-premises, configurações padrão visam facilidade de bootstrap e frequentemente não habilitam criptografia em repouso de `Secrets` no `etcd` nem rotação de logs de auditoria (`--audit-log-maxage`, `--audit-log-maxbackup`).

## Como funciona
Ao rodar nos nós masters, o `kube-bench` verifica a propriedade (`root:root` para PKI e `etcd:etcd` para o diretório de dados `/var/lib/etcd` com permissão `700`) e emite instruções detalhadas de remediação (`== Remediations master ==`) para cada controle reprovado.

## Exemplo
```bash
# Filtrar falhas e recomendacoes de remediacao do control plane e etcd:
kubectl logs job/kube-bench-master | grep -E "^\[(FAIL|WARN)\]\s+(1|2)\."
```

## Limites e trade-offs
Aplicar cegamente uma recomendação antiga de flag do `kube-apiserver` (como flags de `PodSecurityPolicy` removidas no Kubernetes 1.25+) faz o pod estático do `kube-apiserver` falhar na inicialização e derruba o control plane.

## Como verificar
Certifique-se sempre de que a versão do benchmark selecionada no `kube-bench` corresponde à versão do Kubernetes do cluster e valide flags do `kube-apiserver` em homologação antes de editar `/etc/kubernetes/manifests/kube-apiserver.yaml`.

## Conexões
- [[kubebench-controles-kubelet-anonymous-auth-webhook-read-only-port]] — Veja também: Aqua kube-bench: Auditoria e Endurecimento do Kubelet (Seção 4: anonymous-auth, authorization-mode e read-only-port).
- [[kubebench-integracao-trivy-operator-compliance-reports-continuo]] — Veja também: Aqua kube-bench: Execução Contínua do CIS Benchmark via Trivy e Trivy Operator no Cluster.

## Fontes
- [Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md) — README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição; consultado em 2026-10-03.
- [kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md) — Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões; consultado em 2026-10-03.
- [Aqua Security kube-bench — Official GitHub Repository](https://github.com/aquasecurity/kube-bench) — Repositório oficial Apache-2.0 do kube-bench; consultado em 2026-10-03.
