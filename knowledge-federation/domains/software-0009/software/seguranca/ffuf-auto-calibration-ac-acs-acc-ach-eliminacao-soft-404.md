---
id: software.seguranca.tranche04.000333
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/ffuf/ffuf/master/README.md", "https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example", "https://github.com/ffuf/ffuf/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ffuf: Auto-Calibration (`-ac`, `-acs`, `-acc` e `-ach`) para Eliminação Automática de Falso Positivo

## Em uma frase
O recurso de *Auto-Calibration* (`-ac`) do `ffuf` envia sondas preliminares com strings aleatórias inexistentes antes do fuzzing principal para aprender automaticamente o tamanho, número de palavras ou linhas das respostas de erro padrão do servidor.

## Por que importa
Elimina a necessidade de inspecionar manualmente o *baseline* de erro de cada alvo, sendo indispensável ao varrer dezenas de hosts diferentes em lote (`-ach` *per-host autocalibration*).

## Como funciona
Quando `-ac` é ativado, o `ffuf` testa payloads sintéticos (ex.: `randomtest`, `.htaccessrandom`, `adminrandom`) e configura dinamicamente filtros `-fs`, `-fw` ou `-fl` correspondentes. O operador pode adicionar strings customizadas de calibração com `-acc` ou estratégias específicas com `-acs`, e ativar `-ach` quando múltiplos domínios são testados na mesma execução.

## Exemplo
```bash
# Fuzzing multi-host com auto-calibração individual por host (-ach)
ffuf -w hosts.txt:HOST -w paths.txt:PATH \
  -u https://HOST/PATH \
  -ac -ach \
  -mc 200,301,302,403
```

## Limites e trade-offs
Se uma string de auto-calibração customizada (`-acc admin`) coincidir com um endpoint realmente existente no servidor, o `ffuf` calibrará o filtro sobre uma resposta válida e poderá ocultar achados legítimos de mesmo tamanho.

## Como verificar
Execute `ffuf` com `-ac -v` e verifique no cabeçalho inicial da execução quais filtros automáticos (`Calibrated filter: ...`) foram registrados antes do início da wordlist.

## Conexões
- [[ffuf-matchers-filters-status-size-words-lines-regex-time]] — Veja também: ffuf: Precisão com Matchers (`-mc`, `-ms`, `-mw`, `-ml`, `-mr`, `-mt`) e Filters (`-fc`, `-fs`, `-fw`, `-fl`, `-fr`, `-ft`).
- [[ffuf-descoberta-virtual-hosts-vhost-host-header-sni]] — Veja também: ffuf: Descoberta de Virtual Hosts (`Host: FUZZ`) sem Registros DNS Públicos e TLS SNI (`-sni`).
- [[ffuf-modos-multi-wordlist-clusterbomb-pitchfork-sniper-encoders]] — Referência cruzada direta com ffuf-modos-multi-wordlist-clusterbomb-pitchfork-sniper-encoders.

## Fontes
- [ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)](https://raw.githubusercontent.com/ffuf/ffuf/master/README.md) — README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos; consultado em 2026-10-03.
- [ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)](https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example) — Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf; consultado em 2026-10-03.
- [ffuf Official Wiki — Advanced Usage & Configuration Guide](https://github.com/ffuf/ffuf/wiki) — Documentação oficial da wiki do projeto ffuf; consultado em 2026-10-03.
