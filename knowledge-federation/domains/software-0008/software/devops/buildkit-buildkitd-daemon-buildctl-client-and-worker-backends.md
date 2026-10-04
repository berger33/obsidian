---
id: software.devops.tranche04.000352
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

# Arquitetura buildkitd e buildctl com workers OCI (runc/crun) e containerd

## Em uma frase
O BuildKit é composto pelo daemon **`buildkitd`** (disponível para Linux e Windows, escutando por padrão a API gRPC em `/run/buildkit/buildkitd.sock` ou via socket TCP/systemd socket activation) e pelo cliente de linha de comando **`buildctl`** (disponível para Linux, macOS e Windows; no macOS o daemon pode rodar dentro de uma VM Linux via Lima com `limactl start template://buildkit`). O daemon `buildkitd` suporta dois backends de worker: o worker **OCI** (usando `runc` ou `crun`), que é habilitado por padrão, e o worker **containerd**, selecionável com as flags `--oci-worker=false --containerd-worker=true`.

## Por que importa
Desacoplar o cliente leve `buildctl` do daemon `buildkitd` permite que máquinas de desenvolvedores em macOS/Windows ou jobs leves de CI enviem contextos de build via gRPC para frotas remotas de `buildkitd` em Linux, escolhendo entre execução OCI direta ou integração nativa com o image store do `containerd`.

## Como funciona
Em servidores dedicados de build baseados em `containerd`, inicie o `buildkitd` com `--oci-worker=false --containerd-worker=true` quando desejar compartilhar o content store e image store do containerd; caso contrário, utilize o worker OCI padrão com `runc` ou `crun`.

## Exemplo
Uma equipe de plataforma implanta pods `buildkitd` em Kubernetes e configura os jobs de CI para invocarem `buildctl --addr tcp://buildkitd:1234 build ...`, centralizando o cache de compilação e eliminando o uso de Docker-in-Docker privilegiado.

## Limites e trade-offs
Ao expor o `buildkitd` como serviço TCP na rede (`tcp://...`), nunca o deixe sem autenticação mútua TLS (mTLS), pois quem tem acesso à API gRPC do `buildkitd` pode executar processos arbitrários nos workers de build.

## Como verificar
Verifique que o daemon está respondendo executando `buildctl debug workers` contra o socket `/run/buildkit/buildkitd.sock` e confirme o backend ativo (`oci` ou `containerd`).

## Conexões
- [[buildkit-llb-intermediate-format-and-concurrent-solver]] — Veja também: Representação intermediária binária LLB e resolução concorrente de dependências no BuildKit.
- [[buildkit-dockerfile-v0-and-gateway-v0-extensible-frontends]] — Veja também: Frontends extensíveis no BuildKit: dockerfile.v0, gateway.v0 e linguagens alternativas para LLB.

## Fontes
- [Moby BuildKit GitHub — README.md (Architecture, LLB, Frontends, Outputs & Caching)](https://raw.githubusercontent.com/moby/buildkit/master/README.md) — README oficial do Moby BuildKit detalhando arquitetura buildkitd e buildctl, formato intermediário binário LLB em Protobuf, gateway.v0 e dockerfile.v0, backends OCI (runc/crun) e containerd, opções de output (image, local, compression gzip/estargz/zstd, SOURCE_DATE_EPOCH) e export/import de cache.; consultado em 2026-10-03.
- [Go Package Documentation — github.com/moby/buildkit/client/llb](https://pkg.go.dev/github.com/moby/buildkit/client/llb) — Documentação oficial da biblioteca Go client/llb do BuildKit para construção programática de grafos de dependência LLB.; consultado em 2026-10-03.
- [Moby BuildKit — Official GitHub Repository](https://github.com/moby/buildkit) — Repositório oficial Apache-2.0 do Moby BuildKit.; consultado em 2026-10-03.
