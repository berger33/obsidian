---
id: software.devops.tranche08.000735
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/youki-dev/youki/main/README.md", "https://youki-dev.github.io/youki/user/basic_setup.html", "https://github.com/youki-dev/youki"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Youki: execução de containers em modo rootless e integração com Docker e Podman

## Em uma frase
O `youki` suporta a execução de containers sem privilégios de superusuário via `youki spec --rootless` e `youki run`, além de integrar-se diretamente ao Docker (`dockerd --add-runtime`) e ao Podman (`--runtime`).

## Por que importa
Desenvolvedores e operadores de segurança desejam testar e rodar o `youki` tanto diretamente em modo rootless (sem `sudo`) quanto conectado aos seus motores de container favoritos (Docker e Podman) sem precisar montar OCI bundles manualmente para cada imagem. As seções `Quick Start`, `Rootless container` e `Usage` do README oficial do `youki` documentam ambos os fluxos.

## Como funciona
Para executar um container em **modo rootless** diretamente com o `youki`, após preparar o diretório `tutorial/rootfs`, o usuário comum executa `../youki spec --rootless` (que gera um `config.json` configurado com user namespaces e mapeamentos de UID/GID sem privilégios de root) e inicia o container com `../youki run rootless-container`. Para usar o `youki` como runtime do **Docker**, inicia-se o daemon com `dockerd --experimental --add-runtime="youki=$(pwd)/youki"` (parando antes o daemon padrão com `sudo systemctl stop docker` caso `/var/run/docker.pid` já exista) e executa-se `docker run -it --rm --runtime youki busybox`. No **Podman**, basta passar o caminho do binário em `--runtime`, como `sudo podman run --cgroup-manager=cgroupfs --runtime /workspaces/youki/youki hello-world`.

## Exemplo
```bash
# Gerar config.json em modo rootless com youki spec --rootless e executar sem sudo
cd tutorial
../youki spec --rootless
../youki run rootless-container

# Executar um container via Podman apontando diretamente para o binário do youki
sudo podman run --cgroup-manager=cgroupfs --runtime $(pwd)/youki hello-world
```

## Limites e trade-offs
Conforme alerta a seção `Usage` do README oficial do `youki`, ao testar o `youki` iniciando manualmente `dockerd --experimental --add-runtime="youki=$(pwd)/youki"` em um terminal, se o serviço padrão do Docker já estiver ativo via systemd, ocorrerá o erro `failed to start daemon: pid file found, ensure docker is not running or delete /var/run/docker.pid`; em servidores permanentes, é preferível registrar o runtime `youki` em `/etc/docker/daemon.json` e recarregar o serviço systemd.

## Como verificar
Execute `docker run --rm --runtime youki hello-world` (ou o equivalente com `podman --runtime`) e confirme a execução e saída limpa do container gerenciado pelo `youki`.

## Conexões
- [[youki-ciclo-vida-containers-spec-create-start-state-delete]] — Veja também: Youki: geração de especificação (youki spec) e operações de ciclo de vida OCI (create, state, start, list, delete).
- [[youki-oci-spec-rs-tipagem-forte-especificacao-rust]] — Veja também: Youki: crate oci-spec-rs para serialização e validação tipada das especificações OCI Runtime e Image em Rust.
- [[youki-runtime-oci-rust-seguranca-memoria]] — Referência cruzada direta com youki-runtime-oci-rust-seguranca-memoria.
- [[runc-containers-rootless-user-namespaces-configuracao]] — Referência cruzada direta com runc-containers-rootless-user-namespaces-configuracao.

## Fontes
- [Youki GitHub — README.md (OCI Runtime in Rust, Hyperfine Benchmark, Lifecycle, Rootless & Docker/Podman)](https://raw.githubusercontent.com/youki-dev/youki/main/README.md) — README oficial do youki documentando motivação de segurança de memória em Rust, benchmark hyperfine frente a runc e crun, compilação com just, ciclo de vida OCI, modo rootless e youki info; consultado em 2026-10-03.
- [Youki Official User & Developer Documentation — Basic Setup & Architecture](https://youki-dev.github.io/youki/user/basic_setup.html) — Documentação oficial do projeto youki (CNCF Sandbox) e crate associada youki-dev/oci-spec-rs; consultado em 2026-10-03.
- [Youki — Official GitHub Repository](https://github.com/youki-dev/youki) — Repositório oficial Apache-2.0 do runtime OCI youki em Rust; consultado em 2026-10-03.
