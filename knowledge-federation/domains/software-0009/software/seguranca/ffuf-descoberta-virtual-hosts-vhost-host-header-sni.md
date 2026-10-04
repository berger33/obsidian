---
id: software.seguranca.tranche04.000334
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

# ffuf: Descoberta de Virtual Hosts (`Host: FUZZ`) sem Registros DNS Públicos e TLS SNI (`-sni`)

## Em uma frase
O `ffuf` descobre *Virtual Hosts* (vhosts) internos hospedados em proxies reversos Nginx, Apache, Envoy ou ALB mesmo quando os subdomínios não estão publicados no DNS público, realizando fuzzing no cabeçalho HTTP `Host: FUZZ.dominio.corp`.

## Por que importa
Muitas organizações ocultam painéis administrativos (`admin.interno.corp`, `staging-api.corp`) apenas omitindo o registro DNS público, mas apontam o proxy reverso da borda para o mesmo IP público que aceita o cabeçalho `Host`.

## Como funciona
Ao enviar requisições para o endereço IP ou domínio principal (`-u https://203.0.113.10`) variando `-H "Host: FUZZ.corp.internal"`, o servidor HTTP seleciona o bloco `server_name` correspondente se o vhost existir, retornando um tamanho de resposta ou código de status diferente do vhost padrão (*default_server*), que é descartado via `-ac` ou `-fs`.

## Exemplo
```bash
# Descobrir virtual hosts internos em um proxy reverso filtrando a resposta padrão com -ac
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  -u https://203.0.113.10/ \
  -H "Host: FUZZ.corp.internal" \
  -sni corp.internal \
  -ac -mc all
```

## Limites e trade-offs
Se a flag `-r` (seguir redirecionamentos HTTP 301/302) estiver habilitada durante a descoberta de vhosts sem DNS público, o `ffuf` tentará resolver o novo hostname via DNS e falhará; mantenha `-r` desabilitado ao testar vhosts não registrados.

## Como verificar
Execute o comando sem `-r` e confirme que vhosts existentes aparecem com `Status: 200` ou `Status: 302` (exibindo o `Location` com `-v`) e tamanho distinto do vhost padrão.

## Conexões
- [[ffuf-auto-calibration-ac-acs-acc-ach-eliminacao-soft-404]] — Veja também: ffuf: Auto-Calibration (`-ac`, `-acs`, `-acc` e `-ach`) para Eliminação Automática de Falso Positivo.
- [[ffuf-fuzzing-parametros-get-post-json-headers-raw-request]] — Veja também: ffuf: Fuzzing de Parâmetros GET, Payloads POST JSON, Headers Customizados e Requisições Raw (`-request`).
- [[ffuf-matchers-filters-status-size-words-lines-regex-time]] — Referência cruzada direta com ffuf-matchers-filters-status-size-words-lines-regex-time.
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Referência cruzada direta com subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas.

## Fontes
- [ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)](https://raw.githubusercontent.com/ffuf/ffuf/master/README.md) — README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos; consultado em 2026-10-03.
- [ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)](https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example) — Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf; consultado em 2026-10-03.
- [ffuf Official Wiki — Advanced Usage & Configuration Guide](https://github.com/ffuf/ffuf/wiki) — Documentação oficial da wiki do projeto ffuf; consultado em 2026-10-03.
