---
id: software.testes.tranche24.001811
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

# O syz-manager: um binário, um arquivo .cfg

## Em uma frase
A seção Running de docs/usage.md define o ponto de partida: "Start the syz-manager process as ./bin/syz-manager -config my.cfg" — o processo "will wind up VMs and start fuzzing in them", com a localização do arquivo de configuração passada pela opção -config e a configuração em si documentada na página configuration.md do repositório.

## Por que importa
Concentrar a campanha num gerenciador com um config declarativo torna o fuzzing de kernel replicável: a descrição da campanha (VMs, imagem, alvo) versiona junto do código, em vez de viver numa linha de comando de duzentos flags.

## Como funciona
Escreva o my.cfg declarando VM e kernel-alvo conforme configuration.md, inicie ./bin/syz-manager -config my.cfg e acompanhe o log; o mesmo padrão de um processo gerenciador vale para campanhas longas em servidor dedicado.

## Exemplo
Rodada típica de laboratório: config aponta qemu com imagem de kernel com as opções de debug necessárias, e o gerenciador cuida de subir e derrubar instâncias para cada teste de programa.

## Limites e trade-offs
Os campos do config não estão reproduzidos aqui; configuration.md é a referência citada pela nota, e a configuração correta depende de kernel e hypervisor específicos do ambiente.

## Como verificar
A linha de comando e a frase do wind-up de VMs vêm literalmente da seção Running de docs/usage.md oficial.

## Conexões
- [[syzkaller-what-it-is]] — Veja também: syzkaller: fuzzing de kernel não supervisionado e guiado por cobertura.
- [[syzkaller-http-dashboard]] — Veja também: HTTP de serviço: crashes e estatísticas expostos.

## Fontes
- [syzkaller — How to use syzkaller (docs/usage.md)](https://raw.githubusercontent.com/google/syzkaller/master/docs/usage.md) — Guia oficial docs/usage.md do syzkaller sobre execução do syz-manager, painel HTTP, reprodução automática em VMs, reproducers C/syzkaller e hub.; consultado em 2026-10-03.
- [syzkaller — README oficial](https://raw.githubusercontent.com/google/syzkaller/master/README.md) — README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.; consultado em 2026-10-03.
