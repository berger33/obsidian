---
id: software.devops.tranche07.000686
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

# OpenContainer runc: customização de compilação com RUNC_BUILDTAGS, EXTRA_VERSION e tags obsoletas

## Em uma frase
A compilação do `runc` permite adicionar ou remover funcionalidades via variável `RUNC_BUILDTAGS` (`seccomp`, `libpathrs`, `runc_nocriu`) e customizar a string de versão com `EXTRA_VERSION`, tendo tornado AppArmor e SELinux sempre ativos por padrão.

## Por que importa
Mantenedores de distribuições Linux e engenheiros de plataformas embarcadas/edge frequentemente precisam compilar binários customizados do `runc` (por exemplo, desativando o suporte a CRIU em sistemas minimalistas ou adicionando um sufixo de versão corporativo), mas muitas vezes utilizam documentações antigas que passam build tags já obsoletas como `apparmor`, `selinux`, `nokmem` ou `runc_nodmz`. O README oficial do `runc` esclarece exatamente quais tags existem hoje e quais foram aposentadas.

## Como funciona
Para modificar o conjunto padrão de tags de build (`seccomp` e `libpathrs`), usa-se a variável `RUNC_BUILDTAGS`, onde tags prefixadas com `-` são removidas do conjunto padrão e as demais são adicionadas: por exemplo, `make RUNC_BUILDTAGS="runc_nocriu -seccomp"` desabilita o suporte a checkpoint/restore via CRIU (`runc_nocriu`) e remove o `seccomp`. Para identificar builds customizados na saída de `runc --version`, passa-se `make EXTRA_VERSION="+build-1"`. O README documenta ainda as quatro build tags obsoletas que não devem mais ser usadas: `apparmor` e `selinux` (sempre habilitadas desde o `runc v1.0.0-rc93`), `nokmem` (configurações de memória de kernel são ignoradas desde `v1.0.0-rc94`) e `runc_nodmz` (o binário `runc dmz` foi removido desde o `runc v1.2.1`).

## Exemplo
```bash
# Compilar o runc adicionando sufixo de versão customizado e desabilitando checkpoint/restore (CRIU)
make EXTRA_VERSION="+prod-1" RUNC_BUILDTAGS="runc_nocriu"
sudo make install
/usr/local/sbin/runc --version
```

## Limites e trade-offs
Compilar o `runc` com `RUNC_BUILDTAGS="-seccomp"` para contornar a ausência do pacote `libseccomp-dev` produz um binário incapaz de aplicar perfis seccomp de restrição de syscalls, o que fará com que o `kubelet` ou `containerd` falhem ao tentar iniciar containers que exigem `RuntimeDefault` ou perfis seccomp customizados em produção.

## Como verificar
Após compilar com `make EXTRA_VERSION="+custom-1"`, execute `./runc --version` e confirme que a string `+custom-1` aparece anexada à versão e que o suporte a AppArmor, SELinux e seccomp está ativo.

## Conexões
- [[runc-seguranca-path-safety-libpathrs-seccomp]] — Veja também: OpenContainer runc: segurança de caminhos com a biblioteca Rust libpathrs e filtragem de syscalls com libseccomp.
- [[runc-supervisores-systemd-cgroup-v2-checkpoint-criu]] — Veja também: OpenContainer runc: integração com supervisores systemd, cgroup v2 e Checkpoint/Restore com CRIU.
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.
- [[runc-testes-integracao-bats-rootless-go-modules]] — Referência cruzada direta com runc-testes-integracao-bats-rootless-go-modules.

## Fontes
- [OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)](https://raw.githubusercontent.com/opencontainers/runc/main/README.md) — README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd; consultado em 2026-10-03.
- [Open Container Initiative — Runtime Specification (runtime-spec)](https://github.com/opencontainers/runtime-spec) — Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json; consultado em 2026-10-03.
- [OpenContainer runc — Official GitHub Repository](https://github.com/opencontainers/runc) — Repositório oficial Apache-2.0 do runc na Open Container Initiative; consultado em 2026-10-03.
