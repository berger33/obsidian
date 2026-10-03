---
id: software.devops.tranche07.000684
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
fontes: ["https://raw.githubusercontent.com/opencontainers/runc/main/README.md", "https://github.com/opencontainers/runtime-spec", "https://github.com/opencontainers/runc"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenContainer runc: execução de containers rootless com User Namespaces (CONFIG_USER_NS)

## Em uma frase
O `runc` suporta a execução de containers sem privilégios de root (`rootless`) utilizando User Namespaces do kernel Linux (`CONFIG_USER_NS=y`), `runc spec --rootless` e diretório de estado gravável pelo usuário (`--root`).

## Por que importa
Executar o runtime de containers como `root` no host significa que qualquer vulnerabilidade de escape no runtime ou na configuração de volumes pode conceder ao invasor controle total (`UID 0`) sobre o servidor hospedeiro. Segundo a seção `Rootless containers` do README oficial do `runc`, o modo rootless permite que um usuário comum sem privilégios crie e execute containers isolados.

## Como funciona
Para que o modo rootless funcione, o kernel Linux deve ter suporte a User Namespaces compilado e habilitado (`CONFIG_USER_NS=y` em `/proc/config.gz`, com `unprivileged_userns_clone=1` em Arch/Debian ou `user.max_user_namespaces` > 0 em RHEL/CentOS). O usuário comum cria o diretório do bundle em sua home (`~/mycontainer`), extrai o `rootfs` e executa `runc spec --rootless`, que gera um `config.json` adaptado para usuários não privilegiados (incluindo o mapeamento do UID/GID do usuário atual para o `uid 0` dentro do user namespace do container e removendo opções de mount/rede que exigiriam root no host). Na execução, como o diretório padrão `/run/runc` pertence ao root, passa-se a flag global `--root /tmp/runc` apontando para um diretório de estado gravável pelo usuário comum.

## Exemplo
```bash
# Gerar especificação rootless e iniciar um container como usuário comum sem sudo
mkdir -p ~/mycontainer/rootfs
cd ~/mycontainer
docker export $(docker create alpine:latest) | tar -C rootfs -xf -

runc spec --rootless
runc --root /tmp/runc-$USER run mycontainerid
```

## Limites e trade-offs
No modo rootless puro gerado por `runc spec --rootless`, o usuário não privilegiado não possui permissão no kernel para criar interfaces de rede no host nem manipular cgroups sem delegação prévia do systemd (cgroup v2 delegation); por isso, o template rootless padrão compartilha ou isola recursos dentro dos limites permitidos ao UID do usuário no host.

## Como verificar
Como usuário não-root, execute `runc spec --rootless` e inspecione a seção `linux.namespaces` e `linux.uidMappings` no `config.json` para confirmar o mapeamento do seu `uid` do host para `containerID: 0`.

## Conexões
- [[runc-ciclo-vida-create-start-list-delete-run]] — Veja também: OpenContainer runc: operações de ciclo de vida OCI (create, start, list, delete) versus comando composto run.
- [[runc-seguranca-path-safety-libpathrs-seccomp]] — Veja também: OpenContainer runc: segurança de caminhos com a biblioteca Rust libpathrs e filtragem de syscalls com libseccomp.
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.
- [[runc-oci-bundle-rootfs-config-json-runc-spec]] — Referência cruzada direta com runc-oci-bundle-rootfs-config-json-runc-spec.

## Fontes
- [OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)](https://raw.githubusercontent.com/opencontainers/runc/main/README.md) — README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd; consultado em 2026-10-03.
- [Open Container Initiative — Runtime Specification (runtime-spec)](https://github.com/opencontainers/runtime-spec) — Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json; consultado em 2026-10-03.
- [OpenContainer runc — Official GitHub Repository](https://github.com/opencontainers/runc) — Repositório oficial Apache-2.0 do runc na Open Container Initiative; consultado em 2026-10-03.
