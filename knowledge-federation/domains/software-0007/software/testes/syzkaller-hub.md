---
id: software.testes.tranche24.001816
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
fontes: ["https://raw.githubusercontent.com/google/syzkaller/master/docs/usage.md", "https://raw.githubusercontent.com/google/syzkaller/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hub: vários syz-managers trocando achados

## Em uma frase
Para quem roda mais de uma instância, a doc de uso traz o mecanismo Hub: "there's a way to connect them together and allow to exchange programs and reproducers", com detalhes no documento docs/hub.md do repositório.

## Por que importa
Fuzzar o mesmo kernel em máquinas ou configurações diferentes gera corpus complementares; compartilhar programas (e reproducers prontos) entre gerenciadores transforma N campanhas isoladas numa única busca federada, sem sincronizar discos nem dumps.

## Como funciona
Para federar, conecte os syz-managers de acordo com o protocolo do hub.md — cada instância passa a se beneficiar dos programas descobertos pelas outras, incluindo a fase de reprodução que consome VMs.

## Exemplo
Duas campanhas: uma no kernel com KMSAN, outra com KFENCE; o hub permite que um programa gerado por uma ajude a outra a reproduzir o crash equivalente.

## Limites e trade-offs
Os detalhes de topologia, segurança e protocolo do hub não constam do trecho da doc de uso que anuncia o recurso; hub.md é o documento canônico a ler antes de expor portas.

## Como verificar
A seção Hub de docs/usage.md oficial descreve o propósito e referencia o documento próprio.

## Conexões
- [[syzkaller-repro-timing]] — Veja também: Quanto custa reproduzir: de minutos a uma hora.
- [[syzkaller-docs-map]] — Veja também: O mapa da documentação por sistema operacional.

## Fontes
- [syzkaller — How to use syzkaller (docs/usage.md)](https://raw.githubusercontent.com/google/syzkaller/master/docs/usage.md) — Guia oficial docs/usage.md do syzkaller sobre execução do syz-manager, painel HTTP, reprodução automática em VMs, reproducers C/syzkaller e hub.; consultado em 2026-10-03.
- [syzkaller — README oficial](https://raw.githubusercontent.com/google/syzkaller/master/README.md) — README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.; consultado em 2026-10-03.
