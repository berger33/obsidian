---
id: software.devops.tranche08.000720
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
fontes: ["https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md", "https://github.com/firecracker-microvm/firecracker/blob/main/docs/prod-host-setup.md", "https://github.com/firecracker-microvm/firecracker"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# AWS Firecracker: cadência de releases, configuração segura do host (prod-host-setup) e política de segurança

## Em uma frase
O Firecracker publica novas versões a cada dois ou três meses segundo `docs/RELEASE_POLICY.md`, documenta o endurecimento obrigatório do host Linux em `docs/prod-host-setup.md` e trata divulgações de vulnerabilidades sob prioridade máxima (`SECURITY.md`).

## Por que importa
Em uma infraestrutura multi-tenant serverless, rodar uma versão antiga do VMM ou deixar mitigações de canais laterais de CPU (side-channels como Spectre/Meltdown/MDS/L1TF), swap ou configurações de rede mal ajustadas no kernel Linux hospedeiro compromete as garantias de isolamento das microVMs. O README oficial do Firecracker enfatiza a leitura obrigatória de `docs/prod-host-setup.md`, `docs/RELEASE_POLICY.md` e `SECURITY.md`.

## Como funciona
As releases oficiais do Firecracker são publicadas na página de Releases do GitHub tipicamente a cada **dois ou três meses**, acompanhadas de histórico detalhado no `CHANGELOG.md` e regidas pela política de suporte em `docs/RELEASE_POLICY.md`. Para ambientes de produção, o documento `docs/prod-host-setup.md` estabelece as configurações de kernel e sistema operacional hospedeiro necessárias para atingir o patamar de computação multi-tenant segura (incluindo desativação de swap para evitar vazamento de páginas de memória entre tenants em disco, ajustes de SMT/mitigações de vulnerabilidades de execução especulativa de CPU, limites de descritores e regras de iptables/conntrack).

## Exemplo
```bash
# Verificar no host Linux de produção se o swap está desativado e inspecionar mitigações de vulnerabilidades de CPU
swapon --show
grep . /sys/devices/system/cpu/vulnerabilities/*
```

## Limites e trade-offs
Aplicar todas as mitigações mais estritas de hardware/CPU para isolamento multi-tenant hostil (como desabilitar Simultaneous Multithreading — SMT/Hyper-Threading — ou ativar barreiras de agendamento de core contra ataques de canal lateral L1TF/MDS) reduz a capacidade bruta de threads lógicas do servidor físico, exigindo pesar o perfil de ameaça das cargas executadas (código interno confiável versus código arbitrário de terceiros).

## Como verificar
Audite os nós bare-metal que executam o Firecracker contra a checklist oficial em `docs/prod-host-setup.md` e valide a versão do binário `firecracker` em relação à release suportada mais recente.

## Conexões
- [[firecracker-integracao-container-runtimes-kata-flintlock]] — Veja também: AWS Firecracker: integração com runtimes de containers e microVMs (Kata Containers e Flintlock).
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.
- [[firecracker-jailer-isolamento-cgroups-namespaces-seccomp]] — Referência cruzada direta com firecracker-jailer-isolamento-cgroups-namespaces-seccomp.
- [[firecracker-plataformas-testadas-intel-amd-graviton-kernels]] — Referência cruzada direta com firecracker-plataformas-testadas-intel-amd-graviton-kernels.

## Fontes
- [AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)](https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md) — README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton; consultado em 2026-10-03.
- [AWS Firecracker Documentation — Design, Specification & Production Host Setup](https://github.com/firecracker-microvm/firecracker/blob/main/docs/prod-host-setup.md) — Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker; consultado em 2026-10-03.
- [AWS Firecracker — Official GitHub Repository](https://github.com/firecracker-microvm/firecracker) — Repositório oficial do VMM Firecracker mantido pela AWS; consultado em 2026-10-03.
