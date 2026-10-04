---
id: software.testes.tranche07.000117
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html", "https://www.w3.org/WAI/tutorials/forms/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de acessibilidade de autenticação", "Teste: Teste de acessibilidade de autenticação"]
lote: software-testes-2000-0001
---

# Teste de acessibilidade de autenticação

## Em uma frase
Verifique se o processo de autenticação evita exigir uma função cognitiva sem alternativa ou apoio permitido pelo critério de acessibilidade aplicável.

## Por que importa
Desafios de memória, transcrição ou resolução de tarefas podem excluir usuários com limitações cognitivas mesmo quando a página de login parece visualmente simples.

## Como funciona
Mapeie cada etapa de login, MFA, CAPTCHA e recuperação. Teste preenchimento por gerenciador de senhas, colagem e autenticação por alternativas compatíveis; confira exceções e mecanismos permitidos na SC 3.3.8, sem tratar todo método adicional como proibido.

## Exemplo
Use um ambiente de teste para entrar com senha gerada por gerenciador e código de MFA copiável; confirme que a interface não bloqueia colar e oferece alternativa acessível quando uma etapa exige reconhecimento ou recordação.

## Limites e trade-offs
A SC 3.3.8 contém exceções e não exige remover toda autenticação; segurança pode requerer fatores adicionais. A avaliação precisa mapear o critério e o nível de conformidade adotado pelo produto.

## Como verificar
Execute o fluxo completo com teclado e tecnologia assistiva, confirme suporte a mecanismos de autenticação e documente qual exceção normativa, se houver, sustenta cada barreira cognitiva.

## Conexões
- [[teste-acessibilidade-navegacao-teclado]] — aprofundamento relacionado.
- [[teste-acessibilidade-rotulos-erros-formulario]] — aprofundamento relacionado.

## Fontes
- [W3C WAI — Understanding Accessible Authentication](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) — alternativas a testes de função cognitiva na autenticação; consultado em 2026-10-01.
- [W3C WAI — Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/) — rótulos, instruções, validação e notificações em formulários; consultado em 2026-10-01.
