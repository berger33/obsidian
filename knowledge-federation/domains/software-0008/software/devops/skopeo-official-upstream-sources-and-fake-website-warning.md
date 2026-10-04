---
id: software.devops.tranche06.000549
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/containers/skopeo/main/README.md", "https://github.com/containers/image_build/blob/main/skopeo/README.md", "https://github.com/containers/skopeo"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Alerta de segurança upstream do Skopeo: ausência de site separado e rejeição de sites falsos não afiliados

## Em uma frase
Na seção *Obtaining skopeo*, o README oficial traz um alerta crítico de segurança e procedência (supply chain security): **o Skopeo NÃO possui um website separado do projeto** (`Skopeo has no separate project website`). O repositório oficial no GitHub (`github.com/containers/skopeo` / `podman-container-tools/skopeo`) e as imagens de contêiner documentadas em **`quay.io/skopeo/stable`** (junto com os pacotes oficiais das distribuições Linux confiáveis documentadas em `install.md`) são as **únicas builds upstream oficiais**. O README adverte expressamente que **quaisquer outros websites que se apresentem como a página oficial do Skopeo ou ofereçam downloads próprios de binários do Skopeo não têm qualquer afiliação com o projeto**.

## Por que importa
Ferramentas populares de infraestrutura e segurança que não mantêm um domínio `.io`/`.org` próprio frequentemente são alvo de *typosquatting* e sites falsos otimizados para mecanismos de busca que distribuem binários adulterados com malware para engenheiros DevOps desavisados.

## Como funciona
Instale o `skopeo` exclusivamente através do gerenciador de pacotes oficial da sua distribuição Linux (`apt`, `dnf`, `apk`, `pacman`, `zypper`) ou via Homebrew oficial conforme `install.md`, ou utilize a imagem de contêiner oficial **`quay.io/skopeo/stable`**, bloqueando downloads de sites de terceiros não afiliados.

## Exemplo
Ao construir um estágio de pipeline em Kubernetes que precisa rodar o Skopeo em contêiner, o engenheiro referencia exclusivamente a imagem upstream oficial `quay.io/skopeo/stable` indicada no README do repositório `containers/skopeo`.

## Limites e trade-offs
Sempre instrua novos membros da equipe de plataforma sobre o aviso oficial do README do Skopeo para que nunca baixem executáveis avulsos de sites externos encontrados em buscas web.

## Como verificar
Verifique a origem do pacote `skopeo` instalado na máquina (`dpkg -S $(which skopeo)` ou `rpm -qf $(which skopeo)`) ou o repositório da imagem (`quay.io/skopeo/stable`) nos manifestos de CI.

## Conexões
- [[skopeo-containers-storage-interoperability-with-podman-buildah-crio]] — Veja também: Interoperabilidade direta com o backend containers-storage de Podman, Buildah e CRI-O.
- [[skopeo-container-image-usage-quay-skopeo-stable-in-ci]] — Veja também: Execução do Skopeo em contêiner (quay.io/skopeo/stable) para pipelines CI/CD e Tekton Tasks.

## Fontes
- [Skopeo GitHub — README.md (Daemonless & Rootless Image Operations, 6 Storage Transports, Inspect, Copy, Sync & Auth)](https://raw.githubusercontent.com/containers/skopeo/main/README.md) — README oficial do Skopeo (Apache-2.0) detalhando operações em imagens OCI e Docker v2 sem exigir root nem daemon, os 6 tipos de transporte (containers-storage:, dir:, docker://, docker-archive:, docker-daemon:, oci:), inspeção remota sem pull (skopeo inspect e --config), cópia entre registros/transportes (skopeo copy), sincronização air-gapped (skopeo sync), autenticação ($XDG_RUNTIME_DIR/containers/auth.json, --creds, --src-creds, --dest-creds), alerta contra sites falsos não afiliados e tabela dos 11 subcomandos CLI.; consultado em 2026-10-03.
- [Skopeo Official Container Image — containers/image_build/skopeo/README.md](https://github.com/containers/image_build/blob/main/skopeo/README.md) — Documentação oficial da imagem de contêiner upstream do Skopeo publicada em quay.io/skopeo/stable.; consultado em 2026-10-03.
- [Skopeo — Official GitHub Repository](https://github.com/containers/skopeo) — Repositório oficial Apache-2.0 do Skopeo (única fonte upstream oficial junto à imagem quay.io/skopeo/stable).; consultado em 2026-10-03.
