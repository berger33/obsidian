---
id: software.devops.tranche15.001443
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/abiosoft/colima/main/README.md", "https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md", "https://github.com/abiosoft/colima"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Colima: cluster Kubernetes local (`--kubernetes`) e compartilhamento direto de imagens com Docker e containerd

## Em uma frase
A flag `--kubernetes` (`colima start --kubernetes`) provisiona um cluster Kubernetes de nó único dentro da VM do Colima e mescla automaticamente o contexto de acesso no `~/.kube/config` do host.

## Por que importa
Diferentemente do `kind` ou `minikube` padrão — onde imagens construídas localmente no host precisam ser copiadas para dentro dos nós do cluster via `kind load` ou `minikube image load` —, no Colima o Kubernetes compartilha exatamente o mesmo daemon de runtime da VM.

## Como funciona
Quando o Colima roda com o runtime `docker`, qualquer imagem construída com `docker build` ou baixada com `docker pull` fica imediatamente visível para os Pods do Kubernetes sem etapa extra de push/load. Quando roda com `--runtime containerd`, imagens construídas ou baixadas no namespace `k8s.io` (`nerdctl -n k8s.io build`) ficam instantaneamente disponíveis para o Kubelet.

## Exemplo
```bash
colima start --kubernetes
docker build -t local-app:dev .
kubectl run demo --image=local-app:dev --image-pull-policy=Never
kubectl get pods
```

## Limites e trade-offs
Ao usar imagens locais que não existem em nenhum registry remoto, defina `imagePullPolicy: Never` ou `IfNotPresent` no manifesto do Pod (especialmente se usar a tag `:latest`, que por padrão força `Always` no Kubernetes).

## Como verificar
Execute `kubectl config current-context` e `kubectl get nodes` após `colima start --kubernetes` para validar a prontidão do nó `colima`.

## Conexões
- [[colima-runtimes-docker-containerd-nerdctl-incus-selecao]] — Veja também: Colima: seleção de runtimes (`docker`, `containerd` com `nerdctl` e `incus`) na inicialização da instância.
- [[colima-ai-workloads-gpu-krunkit-docker-model-runner-ramalama]] — Veja também: Colima: aceleração por GPU para modelos de IA (`--vm-type krunkit`) com Docker Model Runner e Ramalama.

## Fontes
- [Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)](https://raw.githubusercontent.com/abiosoft/colima/main/README.md) — README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM; consultado em 2026-10-03.
- [Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)](https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md) — FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento; consultado em 2026-10-03.
- [Colima — Official GitHub Repository](https://github.com/abiosoft/colima) — Repositório oficial MIT do Colima; consultado em 2026-10-03.
