---
id: software.devops.tranche04.000351
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/moby/buildkit/master/README.md", "https://pkg.go.dev/github.com/moby/buildkit/client/llb", "https://github.com/moby/buildkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Representação intermediária binária LLB e resolução concorrente de dependências no BuildKit

## Em uma frase
O BuildKit é um toolkit para converter código-fonte em artefatos de build de maneira eficiente, expressiva e reproduzível, sendo usado por padrão pelo `docker build` (via Buildx e BuildKit) desde o Docker Engine 23.0. O núcleo dos builds no BuildKit baseia-se em um formato intermediário binário chamado **LLB (Low-Level Builder)** — definido em `solver/pb/ops.proto` e serializado como mensagens **Protobuf** — que modela o grafo de dependências entre processos que executam partes do build. Como resume a documentação oficial: **"LLB is to Dockerfile what LLVM IR is to C"** — sendo executável concorrentemente, eficientemente armazenável em cache e neutro em relação a fornecedor ou linguagem de frontend.

## Por que importa
O antigo builder sequencial processava cada linha de um Dockerfile em série, mesmo quando dois estágios eram independentes. Ao compilar a definição de build para um grafo acíclico direcionado (DAG) em LLB, o solver do BuildKit executa estágios independentes em paralelo e pula inteiramente ramos cujo resultado final não é consumido pelo alvo.

## Como funciona
Estruture seus Dockerfiles em múltiplos estágios independentes (por exemplo, download de dependências, compilação de assets frontend e compilação de binário backend) para que o solver LLB do BuildKit os execute de forma concorrente.

## Exemplo
Em um build multi-stage que compila três binários Go independentes antes de copiá-los para uma imagem `scratch` final, o BuildKit converte os estágios em nós LLB paralelos e executa as três compilações simultaneamente, reduzindo o tempo total de build pela metade.

## Limites e trade-offs
Evite encadear estágios em uma única linha linear desnecessária (`FROM stage1 AS stage2`) quando o segundo estágio não depende dos arquivos produzidos pelo primeiro, pois isso impede a execução concorrente no grafo LLB.

## Como verificar
Inspecione o grafo ou a execução concorrente com `buildctl build` e confirme nos logs que os estágios independentes progridem simultaneamente no terminal.

## Conexões
- [[buildkit-buildkitd-daemon-buildctl-client-and-worker-backends]] — Veja também: Arquitetura buildkitd e buildctl com workers OCI (runc/crun) e containerd.

## Fontes
- [Moby BuildKit GitHub — README.md (Architecture, LLB, Frontends, Outputs & Caching)](https://raw.githubusercontent.com/moby/buildkit/master/README.md) — README oficial do Moby BuildKit detalhando arquitetura buildkitd e buildctl, formato intermediário binário LLB em Protobuf, gateway.v0 e dockerfile.v0, backends OCI (runc/crun) e containerd, opções de output (image, local, compression gzip/estargz/zstd, SOURCE_DATE_EPOCH) e export/import de cache.; consultado em 2026-10-03.
- [Go Package Documentation — github.com/moby/buildkit/client/llb](https://pkg.go.dev/github.com/moby/buildkit/client/llb) — Documentação oficial da biblioteca Go client/llb do BuildKit para construção programática de grafos de dependência LLB.; consultado em 2026-10-03.
- [Moby BuildKit — Official GitHub Repository](https://github.com/moby/buildkit) — Repositório oficial Apache-2.0 do Moby BuildKit.; consultado em 2026-10-03.
