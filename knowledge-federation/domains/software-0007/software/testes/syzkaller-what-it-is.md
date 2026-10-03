---
id: software.testes.tranche24.001810
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/google/syzkaller/master/README.md", "https://github.com/google/syzkaller"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# syzkaller: fuzzing de kernel não supervisionado e guiado por cobertura

## Em uma frase
O README oficial define: "syzkaller (IPA: siːzˈkɔːlə) is an unsupervised coverage-guided kernel fuzzer", com SOs suportados listados como FreeBSD, Fuchsia, gVisor, Linux, NetBSD, OpenBSD e Windows — e a nota histórica de que o projeto nasceu focado no kernel Linux e vem sendo estendido aos demais.

## Por que importa
Fuzzing de kernel é a classe em que um bug significa panico de máquina inteira ou escalada de privilégio; "não supervisionado" aqui é projeto: a ferramenta opera VMs, detecta crashes e reproduz sozinha, sem humano no loop de triagem primária.

## Como funciona
A arquitetura separa o gerenciador (orquestra VMs e campanhas), os prog-tester instrumentados rodando dentro da VM e o corpus de programas de syscalls gerados com cobertura de kernel; a configuração vive num arquivo .cfg que o gerenciador recebe na linha de comando.

## Exemplo
Depois do build, o ciclo mínimo é apontar um config para uma imagem de kernel e iniciar o syz-manager — a partir daí a ferramenta fuzza dentro das VMs que ela mesma sobe.

## Limites e trade-offs
A definição não promete detecção de toda classe de bug de kernel: cobertura guiada a syscalls depende da descrição de syscall que acompanha o projeto, e kernels modificados fora das opções suportadas estão fora da garantia do README.

## Como verificar
A frase de definição, a lista de SOs e o contexto histórico Linux-first constam da abertura do README oficial.

## Conexões
- [[syzkaller-manager-config]] — Veja também: O syz-manager: um binário, um arquivo .cfg.

## Fontes
- [syzkaller — README oficial](https://raw.githubusercontent.com/google/syzkaller/master/README.md) — README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.; consultado em 2026-10-03.
- [Repositório oficial google/syzkaller](https://github.com/google/syzkaller) — Repositório oficial do syzkaller no GitHub com código-fonte, descrições de syscalls, integração OSS-Fuzz e documentação.; consultado em 2026-10-03.
