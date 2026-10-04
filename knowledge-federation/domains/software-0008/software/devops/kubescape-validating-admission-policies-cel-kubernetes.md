---
id: software.devops.tranche07.000644
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/kubescape/kubescape/master/README.md", "https://kubescape.io/docs/operator/", "https://github.com/kubescape/kubescape"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubescape: controle de admissão nativo com Validating Admission Policies (VAP) baseadas em CEL

## Em uma frase
O subcomando `kubescape vap` implanta uma biblioteca de políticas CEL (Common Expression Language) e gera bindings de `ValidatingAdmissionPolicy` nativos do Kubernetes para bloquear recursos inseguros no `kube-apiserver`.

## Por que importa
Escanear o cluster periodicamente detecta configurações inseguras depois que os pods já foram implantados, enquanto controladores de admissão baseados em webhooks HTTP externos adicionam latência às requisições da API e criam pontos únicos de falha se o pod do webhook cair. De acordo com o README oficial do Kubescape, o suporte a Validating Admission Policies (VAP) utiliza o mecanismo in-process do próprio Kubernetes baseado em CEL para impor controles da Regolibrary diretamente na admissão.

## Como funciona
O comando `kubescape vap deploy-library` gera os manifestos contendo o conjunto de regras `ValidatingAdmissionPolicy` traduzidas para expressões CEL, que podem ser aplicadas diretamente no cluster via `kubectl apply -f -`. Uma vez que a biblioteca está presente no cluster, o administrador ativa políticas específicas para namespaces ou tipos de recursos usando `kubescape vap create-policy-binding --name <nome> --policy <id-controle> --namespace <ns>`, criando objetos `ValidatingAdmissionPolicyBinding` que instruem o `kube-apiserver` a rejeitar ou auditar imediatamente qualquer `CREATE`/`UPDATE` que viole o controle (como `c-0016` — proibição de containers privilegiados).

## Exemplo
```bash
# Implantar a biblioteca de Validating Admission Policies (CEL) do Kubescape no cluster
kubescape vap deploy-library | kubectl apply -f -

# Criar e aplicar um Policy Binding para o controle c-0016 em um namespace específico
kubescape vap create-policy-binding \
  --name bloquear-privilegiados-prod \
  --policy c-0016 \
  --namespace producao | kubectl apply -f -
```

## Limites e trade-offs
As `ValidatingAdmissionPolicies` baseadas em CEL são avaliadas dentro do próprio processo do `kube-apiserver` com altíssima performance e sem dependência de webhooks de rede, porém exigem versões modernas do Kubernetes onde a API `admissionregistration.k8s.io/v1` (ou `v1beta1`) esteja habilitada e não suportam mutação de objetos nem consultas externas a registries de imagens durante a admissão.

## Como verificar
Verifique os recursos criados com `kubectl get validatingadmissionpolicies,validatingadmissionpolicybindings` e tente aplicar um Pod que viole o controle vinculado no namespace alvo para confirmar a rejeição imediata pelo `kube-apiserver`.

## Conexões
- [[kubescape-auto-remediacao-fix-manifestos-patching-copacetic]] — Veja também: Kubescape: auto-remediação de manifestos (kubescape fix) e patching de imagens com Copacetic (kubescape patch).
- [[kubescape-operador-in-cluster-monitoramento-continuo-helm]] — Veja também: Kubescape Operator: monitoramento contínuo in-cluster de configuração, CVEs e runtime via Helm.
- [[kubescape-plataforma-seguranca-kubernetes-opa-regolibrary]] — Referência cruzada direta com kubescape-plataforma-seguranca-kubernetes-opa-regolibrary.

## Fontes
- [Kubescape GitHub — README.md (OPA/Regolibrary, Grype, Copacetic, VAP, Operator & MCP)](https://raw.githubusercontent.com/kubescape/kubescape/master/README.md) — README oficial do Kubescape documentando varredura de postura com OPA/Regolibrary, CVEs de imagens com Grype, auto-fix, patching com Copacetic, Validating Admission Policies (CEL) e MCP server; consultado em 2026-10-03.
- [Kubescape Official Documentation — In-Cluster Operator & Runtime Security](https://kubescape.io/docs/operator/) — Documentação oficial do operador in-cluster do Kubescape com monitoramento contínuo e detecção de ameaças em runtime via eBPF (Inspektor Gadget); consultado em 2026-10-03.
- [Kubescape — Official GitHub Repository](https://github.com/kubescape/kubescape) — Repositório oficial Apache-2.0 do Kubescape (CNCF Incubating); consultado em 2026-10-03.
