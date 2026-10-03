---
id: software.devops.tranche15.001465
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
fontes: ["https://spegel.dev/docs/getting-started/", "https://raw.githubusercontent.com/spegel-org/spegel/main/README.md", "https://github.com/spegel-org/spegel"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Spegel: verificação funcional de espelhamento P2P e página de diagnóstico `/debug/web`

## Em uma frase
Como o fallback do `containerd` para o registry externo é silencioso, validar que o Spegel está efetivamente servindo imagens entre nós requer disparar pulls sequenciais em dois nós distintos e inspecionar a interface `/debug/web` na porta `9090`.

## Por que importa
Apenas ver o Pod de um mirror em estado `Running` não garante que o `containerd` esteja roteando os pulls por ele; se `certs.d` estiver apontando para o caminho errado, todos os pulls continuarão saindo pela internet sem gerar erro visível no Pod da aplicação.

## Como funciona
O procedimento oficial agenda um primeiro Pod (`upstream`) com `imagePullPolicy: Always` no nó A para popular o cache, em seguida agenda um segundo Pod (`mirror`) com a mesma imagem no nó B, abre `kubectl port-forward` na porta `9090` do Pod do Spegel no nó B e acessa `http://localhost:9090/debug/web`.

## Exemplo
```bash
kubectl --namespace spegel port-forward daemonset/spegel 9090:9090 &
curl -s http://localhost:9090/debug/web | head -n 20
```

## Limites e trade-offs
Se o quadro `Last Mirror Success` em `/debug/web` continuar exibindo `Pending` após o segundo nó baixar a imagem, o pull não passou pelo Spegel e a configuração de `certs.d` do `containerd` precisa ser revisada.

## Como verificar
Confirme que o campo `Last Mirror Success` na página `http://localhost:9090/debug/web` do segundo nó exibe uma duração recente após o teste de pull.

## Conexões
- [[spegel-configuracao-eks-al2023-nodeadm-nodeconfig-bottlerocket]] — Veja também: Spegel: configuração de nós Amazon EKS em AMIs AL2023 (`nodeadm`) e Bottlerocket.
- [[spegel-implantacao-gitops-flux-helmrepository-oci-helmrelease]] — Veja também: Spegel: implantação declarativa via GitOps com Flux (`HelmRepository` OCI e `HelmRelease`).

## Fontes
- [Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)](https://spegel.dev/docs/getting-started/) — Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web; consultado em 2026-10-03.
- [Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)](https://raw.githubusercontent.com/spegel-org/spegel/main/README.md) — README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos; consultado em 2026-10-03.
- [Spegel — Official GitHub Repository](https://github.com/spegel-org/spegel) — Repositório oficial do Spegel; consultado em 2026-10-03.
