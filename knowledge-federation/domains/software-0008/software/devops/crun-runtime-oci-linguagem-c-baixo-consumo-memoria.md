---
id: software.devops.tranche07.000691
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
fontes: ["https://raw.githubusercontent.com/containers/crun/main/README.md", "https://raw.githubusercontent.com/containers/crun/main/crun.1.md", "https://github.com/containers/crun"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Containers crun: runtime OCI escrito inteiramente em C para alta performance e baixo footprint de memória

## Em uma frase
O `crun` (projeto da organização `containers` em conformidade com `opencontainers/runtime-spec`) é um runtime de containers OCI rápido e de baixíssimo consumo de memória escrito inteiramente em linguagem C, podendo também ser embarcado como biblioteca (`libcrun`).

## Por que importa
Embora a maioria das ferramentas do ecossistema de containers Linux seja escrita em Go (como o `runc`), o runtime Go precisa inicializar o coletor de lixo, múltiplas threads de sistema operacional e re-executar a si mesmo usando um módulo em C para configurar namespaces antes que o processo do container inicie. Segundo o README oficial do `crun`, escrever o runtime inteiramente em C reduz o tempo de execução de 100 containers sequenciais `/bin/true` em quase metade (`-49.4%`, de `3.34s` no `runc` para `1.69s` no `crun`) e permite rodar containers com limites estritos de memória nos quais o `runc` falha.

## Como funciona
O `crun` implementa toda a especificação OCI Runtime em C puro (utilizando `libocispec` para gerar o parser C de `config.json` em tempo de compilação, sem depender de Python em tempo de execução) e é o runtime OCI padrão adotado pelo Podman em distribuições modernas como Fedora e RHEL. Por exigir muito menos memória RAM durante a inicialização do container dentro do cgroup recém-criado, o README oficial demonstra que um container com `--memory 4M` falha ao iniciar com `/usr/bin/runc` (pois o próprio processo de init do runtime Go estoura o limite de 4 MB antes de fazer `execve`), enquanto o `/usr/bin/crun` consegue iniciar um container com sucesso usando um limite de apenas `--memory 512k`.

## Exemplo
```bash
# Comparação prática documentada no README do crun executando um container com limite estrito de 512 KB de memória
podman --runtime /usr/bin/crun run --rm --memory 512k fedora echo it works

# Verificar a versão e os recursos suportados pelo binário crun no host Linux
crun --version
```

## Limites e trade-offs
Por ser escrito em C, o desenvolvimento e a manutenção do `crun` exigem gerenciamento rigoroso de memória e ponteiros (auditado continuamente no repositório com Coverity e CodeQL), e a construção das bibliotecas compartilhadas (`libcrun`) não vem habilitada no `./configure` padrão, exigindo passar `./configure --enable-shared` quando se deseja embarcar o `crun` como biblioteca em outros programas ou usar seus bindings Lua/Python.

## Como verificar
Execute `crun --version` para confirmar a versão instalada e teste `podman --runtime /usr/bin/crun run --rm --memory 2M alpine true` para validar a inicialização sob limite restrito de cgroup de memória.

## Conexões
- [[crun-comandos-cli-estado-mounts-dinamicos-update]] — Veja também: Containers crun: comandos de ciclo de vida OCI, diretórios de estado, mounts dinâmicos e update de recursos.
- [[crun-gerenciamento-cgroups-v2-systemd-subgroup-delegation]] — Referência cruzada direta com crun-gerenciamento-cgroups-v2-systemd-subgroup-delegation.
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.

## Fontes
- [Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)](https://raw.githubusercontent.com/containers/crun/main/README.md) — README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG; consultado em 2026-10-03.
- [Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)](https://raw.githubusercontent.com/containers/crun/main/crun.1.md) — Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun); consultado em 2026-10-03.
- [Containers crun — Official GitHub Repository](https://github.com/containers/crun) — Repositório oficial do runtime OCI crun na organização containers; consultado em 2026-10-03.
