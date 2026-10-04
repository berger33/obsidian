---
id: software.devops.tranche13.001234
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
fontes: ["https://d7y.io/docs/next/", "https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md", "https://github.com/dragonflyoss/dragonfly"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Dragonfly: Integração Não-Intrusiva com containerd, CRI-O e Docker para Pull de Imagens OCI

## Em uma frase
O Dragonfly integra-se de forma não-intrusiva aos runtimes de containers (`containerd`, `CRI-O`, `Docker`, `Podman`) configurando o daemon local do Peer (`dfdaemon`) como proxy HTTP/HTTPS ou mirror de registry local em cada nó do Kubernetes.

## Por que importa
Alterar o código das aplicações ou os manifestos de `Deployment` apenas para usar P2P seria inviável; ao interceptar o download de blobs no nível do `containerd`, qualquer Pod agendado no nó se beneficia automaticamente da rede P2P.

## Como funciona
No `containerd`, configura-se o `hosts.toml` do diretório `certs.d` para rotear requisições de download de blobs de camadas (`/v2/.*/blobs/sha256:.*`) para o endpoint local do `dfdaemon` (por exemplo, `http://127.0.0.1:4001`), que intercepta o pull, baixa as peças via malha P2P do Dragonfly e devolve o blob íntegro ao runtime.

## Exemplo
```toml
# Exemplo em /etc/containerd/certs.d/docker.io/hosts.toml apontando para o Peer local:
server = "https://index.docker.io"

[host."http://127.0.0.1:4001"]
  capabilities = ["pull", "resolve"]
  [host."http://127.0.0.1:4001".header]
    X-Dragonfly-Registry = ["https://index.docker.io"]
```

## Limites e trade-offs
Interceptar todas as chamadas do registry sem permitir fallback direto ao registry de origem quando o daemon local do Dragonfly está em manutenção pode impedir o agendamento de novos Pods no nó.

## Como verificar
Mantenha a URL oficial do registry no campo `server` do `hosts.toml` do `containerd` para que o runtime faça fallback seguro para a origem caso o endpoint local `127.0.0.1:4001` esteja indisponível.

## Conexões
- [[dragonfly-load-aware-scheduling-two-stage-parent-selection]] — Veja também: Dragonfly: Algoritmo de Agendamento em Dois Estágios Sensível à Carga (Load-Aware Scheduling).
- [[dragonfly-distribuicao-modelos-ia-ml-huggingface-s3-lfs]] — Veja também: Dragonfly: Aceleração P2P de Pesos de Modelos de IA/ML, Objetos S3/OSS e Datasets em Clusters GPU.

## Fontes
- [Dragonfly GitHub — README.md (P2P File & Image Distribution, Architecture: Manager, Scheduler, Seed Peer & Dfdaemon in Rust)](https://d7y.io/docs/next/) — README oficial do dragonflyoss/dragonfly (CNCF Incubating) descrevendo a arquitetura P2P, cliente Dfdaemon reescrito em Rust (v2.1.0+), isolamento de I/O, integração com Nydus e modelos de IA; consultado em 2026-10-03.
- [Dragonfly Official Documentation — d7y.io/docs/next/ (Quickstart, Containerd Mirror, Preheat & Observability)](https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md) — Documentação oficial do Dragonfly sobre configuração de mirror no containerd, dfget, dfcache, preheat de imagens/modelos e métricas; consultado em 2026-10-03.
- [Dragonfly — Official GitHub Repository](https://github.com/dragonflyoss/dragonfly) — Repositório oficial do Dragonfly na CNCF; consultado em 2026-10-03.
