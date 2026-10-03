---
id: software.seguranca.tranche09.000857
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/sullo/nikto/master/README.md", "https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default", "https://github.com/sullo/nikto/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Nikto: Calibração contra Páginas **"Soft 404"** (`db_404_strings`, `-no404`) e Prefixo de Diretório **`-root`**

## Em uma frase
Um dos maiores desafios para qualquer scanner baseado em existência de caminhos (como o plugin `tests` do Nikto) são servidores web mal configurados ou Single-Page Applications que retornam **`HTTP 200 OK`** para qualquer URL inexistente ("Soft 404"): se o scanner confiar cegamente no código `200`, ele reportará falsamente que o servidor possui 5.000 vulnerabilidades diferentes!

## Por que importa
Antes de iniciar os testes, o Nikto realiza uma fase automática de **Detecção de Página 404**: ele requisita nomes de arquivos aleatórios inexistentes com diferentes extensões (`.html`, `.php`, `.asp`, `.cgi`), calcula o hash MD5 / assinatura do conteúdo retornado e consulta o banco **`db_404_strings`** para remover partes dinâmicas (como timestamps ou a própria URL refletida na página de erro)!

## Como funciona
E quando a aplicação auditada não está na raiz `/` do domínio, mas sim montada sob um sub-caminho (ex.: `https://portal.corp/app-legado/`), passar **`-root /app-legado`** prefixa `/app-legado` em todos os testes do Nikto!

## Exemplo
```bash
# Auditar uma aplicacao montada sob o sub-caminho /sistema-financeiro salvando todas as respostas positivas brutas (-Save)
nikto -h https://portal.internal.corp \
  -root /sistema-financeiro \
  -Save /cases/pentest/nikto_positive_responses \
  -Tuning 123b -Cgidirs none \
  -ask no -nointeractive -nocheck \
  -o /cases/pentest/nikto_root_app.json
```

## Limites e trade-offs
A flag **`-Save <diretorio>`** é extremamente valiosa para eliminar falsos positivos: ela grava no disco os cabeçalhos e o corpo HTTP completo de **cada resposta que acionou um alerta do Nikto**, permitindo ao analista inspecionar o arquivo salvo e confirmar imediatamente se é um achado real ou uma página Soft-404!

## Como verificar
Se uma página Soft-404 customizada da empresa continuar gerando falsos positivos por conter um token dinâmico por requisição, adicione a string característica dela em `udb_404_strings`.

## Conexões
- [[nikto-varredura-autenticada-headers-cookies-mtls-proxies]] — Veja também: Nikto: Varredura Autenticada (**`-id` Basic/NTLM**, **`-Add-header`**, `STATIC-COOKIE`), Certificados de Cliente **mTLS (`-RSAcert`, `-key`)** e **`-useproxy`**.
- [[nikto-varredura-multi-host-multi-porta-nmap-gnmap-maxtime-pause]] — Veja também: Nikto em Lote: Ingestão Direta de Saída **Nmap (`-h scan.gnmap`)**, Múltiplas Portas (`-port 80,443,8080`) e Limites **`-maxtime` / `-Pause`**.
- [[nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins]] — Referência cruzada direta com nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins.
- [[gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length]] — Referência cruzada direta com gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length.
- [[feroxbuster-filtragem-precisa-status-size-words-lines-regex-similar]] — Referência cruzada direta com feroxbuster-filtragem-precisa-status-size-words-lines-regex-similar.

## Fontes
- [Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes](https://raw.githubusercontent.com/sullo/nikto/master/README.md) — documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída; consultado em 2026-10-03.
- [Nikto Official Default Configuration Reference (`nikto.conf.default`)](https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default) — arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker; consultado em 2026-10-03.
- [Nikto Official Project Wiki — Plugins, Databases & Reporting](https://github.com/sullo/nikto/wiki) — wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins; consultado em 2026-10-03.
