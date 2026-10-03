---
id: software.devops.tranche07.000687
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

# OpenContainer runc: integração com supervisores systemd, cgroup v2 e Checkpoint/Restore com CRIU

## Em uma frase
O `runc` integra-se a supervisores de processos como o `systemd` (via units `Type=forking` com `--pid-file` e driver systemd de cgroup), suporta a hierarquia unificada `cgroup v2` e realiza checkpoint/restore de containers em execução com CRIU.

## Por que importa
Como o `runc` não possui um daemon residente para monitorar ou reiniciar containers que saem inesperadamente, ambientes Linux que executam containers OCI diretamente sem Docker/containerd precisam delegar o gerenciamento de ciclo de vida, reinicialização e controle de recursos (cgroups) ao sistema de init do host (`systemd`), além de contar com suporte a congelamento e migração de estado em memória via CRIU. O README oficial do `runc` documenta o uso com supervisores e aponta para a documentação de `cgroup-v2`, `systemd` e `checkpoint-restore`.

## Como funciona
Para supervisionar um container com o `systemd`, cria-se um arquivo de unit `[Service]` com `Type=forking`, `WorkingDirectory=/mycontainer`, `PIDFile=/run/mycontainerid.pid`, `ExecStart=/usr/local/sbin/runc run -d --pid-file /run/mycontainerid.pid mycontainerid` e `ExecStopPost=/usr/local/sbin/runc delete mycontainerid`. Para gerenciamento de recursos, o `runc` suporta plenamente a hierarquia unificada `cgroup v2` e o driver `systemd` (`--systemd-cgroup`), onde as regras de cgroup são solicitadas ao systemd via D-Bus em vez de escritas diretamente no cgroupfs. Além disso, quando compilado sem `runc_nocriu` e com o utilitário **CRIU** instalado no host, `runc checkpoint` e `runc restore` permitem salvar o estado em memória de um container em disco e restaurá-lo posteriormente.

## Exemplo
```ini
# Exemplo oficial de unit file do systemd para supervisionar um container executado com runc
[Unit]
Description=Start My Container

[Service]
Type=forking
ExecStart=/usr/local/sbin/runc run -d --pid-file /run/mycontainerid.pid mycontainerid
ExecStopPost=/usr/local/sbin/runc delete mycontainerid
WorkingDirectory=/mycontainer
PIDFile=/run/mycontainerid.pid

[Install]
WantedBy=multi-user.target
```

## Limites e trade-offs
Ao usar o driver `--systemd-cgroup` (recomendado em distribuições modernas com systemd e cgroup v2, como no Kubernetes com `cgroupDriver: systemd`), todos os componentes da pilha (kubelet, containerd/CRI-O e runc) devem estar configurados de forma idêntica para usar `systemd` e respeitar a regra de escritor único (single-writer rule) do cgroup v2.

## Como verificar
Recarregue o systemd (`sudo systemctl daemon-reload`), inicie o serviço do container e verifique com `systemctl status` e `sudo runc list` se o PID rastreado em `/run/mycontainerid.pid` está ativo e sob o slice esperado no `systemd-cgls`.

## Conexões
- [[runc-compilacao-build-tags-nocriu-obsoletos]] — Veja também: OpenContainer runc: customização de compilação com RUNC_BUILDTAGS, EXTRA_VERSION e tags obsoletas.
- [[runc-testes-integracao-bats-rootless-go-modules]] — Veja também: OpenContainer runc: suíte de testes isolada em container (make test, BATS, rootless) e gestão de dependências Go.
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.
- [[runc-ciclo-vida-create-start-list-delete-run]] — Referência cruzada direta com runc-ciclo-vida-create-start-list-delete-run.
- [[crun-checkpoint-restore-criu-pre-dump-gerenciamento]] — Referência cruzada direta com crun-checkpoint-restore-criu-pre-dump-gerenciamento.

## Fontes
- [OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)](https://raw.githubusercontent.com/opencontainers/runc/main/README.md) — README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd; consultado em 2026-10-03.
- [Open Container Initiative — Runtime Specification (runtime-spec)](https://github.com/opencontainers/runtime-spec) — Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json; consultado em 2026-10-03.
- [OpenContainer runc — Official GitHub Repository](https://github.com/opencontainers/runc) — Repositório oficial Apache-2.0 do runc na Open Container Initiative; consultado em 2026-10-03.
