---
id: software.testes.tranche24.001812
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

# HTTP de serviço: crashes e estatísticas expostos

## Em uma frase
Ainda na seção Running, o README de uso anota: "Found crashes, statistics and other information is exposed on the HTTP address specified in the manager config" — o gerenciador serve um endereço HTTP com a visão operacional da campanha.

## Por que importa
Campanhas de kernel rodam por dias; expor crashes e estatísticas por HTTP transforma o fuzzador num serviço observável — dashboards para a equipe, consulta sem SSH no servidor, e a triagem pode começar por link colado no chat, não por dump de log.

## Como funciona
Configure um endereço HTTP no manager config, mantenha a porta restrita à rede interna e monitore a página de status durante a campanha; é de lá que os reports de crash saem para a triagem.

## Exemplo
Um time de CI de kernel publica a URL interna do syz-manager como artefato de ambiente: qualquer desenvolvedor vê a fila de crashes sem acesso à máquina.

## Limites e trade-offs
A doc de uso declara a exposição do painel; autenticação e endurecimento do serviço HTTP não são cobertos no trecho lido — a responsabilidade de protegê-lo é de quem expõe.

## Como verificar
A frase sobre o endereço HTTP está na seção Running de docs/usage.md oficial.

## Conexões
- [[syzkaller-manager-config]] — Veja também: O syz-manager: um binário, um arquivo .cfg.
- [[syzkaller-auto-repro]] — Veja também: Reprodução automática: 4 VMs e minimização.

## Fontes
- [syzkaller — How to use syzkaller (docs/usage.md)](https://raw.githubusercontent.com/google/syzkaller/master/docs/usage.md) — Guia oficial docs/usage.md do syzkaller sobre execução do syz-manager, painel HTTP, reprodução automática em VMs, reproducers C/syzkaller e hub.; consultado em 2026-10-03.
- [syzkaller — README oficial](https://raw.githubusercontent.com/google/syzkaller/master/README.md) — README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.; consultado em 2026-10-03.
