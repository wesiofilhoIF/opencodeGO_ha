# Changelog

Todas as alterações notáveis deste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.41] - 2026-10-08

### Fixed
- Corrigido erro de API key inválida que aparecia como "Failed to connect" no config flow; agora exibe "Invalid authentication".
- Corrigido `KeyError` ao converter schemas de ferramentas/structured output sem a chave `type` (ex.: `anyOf`, `enum`).
- Corrigido erro em ferramentas sem parâmetros, cujos argumentos chegam vazios da API.
- Corrigido envio de anexos quando a mensagem do usuário não tem texto, que podia anexar os arquivos à mensagem errada ou gerar `AssertionError`.
- Corrigido vazamento do cliente HTTP ao descarregar a integração (`client.close` agora é chamado no unload).
- Declarada a dependência `ai_task` no `manifest.json`, já que a integração importa o componente.
- Aumentado o requisito mínimo do `openai` para `>=1.99.2`, primeira versão com os tipos de tool usados pelo código.
- Corrigido envio de PDFs, que agora usam o tipo `file` (a Chat Completions API não aceita PDF em `image_url`).
- Adicionado `additionalProperties: false` aos schemas de structured output, exigido pelo modo estrito.
- Corrigida a decodificação de respostas do AI Task envoltas em bloco de código Markdown (` ```json `).
- Passou a ser lançado erro quando o limite de iterações de ferramentas é atingido, em vez de encerrar silenciosamente.

### Changed
- Removido bloco `try/except` que apenas relançava a exceção em `_get_models`.

## [1.0.5] - 2026-10-08

### Added
- Adicionado `CHANGELOG.md` com histórico completo de modificações.

## [1.0.4] - 2026-10-08

### Changed
- Migrado o endpoint da API de OpenCode Zen (`https://opencode.ai/zen/v1`) para OpenCode Go (`https://opencode.ai/zen/go/v1`).
- `const.py` passou a ser a única fonte da URL base da API.
- Atualizados metadados do fork (`manifest.json`):
  - `codeowners`: `@airy10` → `@wesiofilhoIF`
  - `documentation` e `issue_tracker` apontam para `wesiofilhoIF/opencodeGO_ha`
- Reescrito o `README.md` com instruções completas de instalação, configuração e solução de problemas em português.
- Atualizadas traduções (`strings.json` e `en.json`) para referenciar "OpenCode Go API key".
- Atualizado template de bug report para o nome do fork.

### Removed
- Removido `extra_body: {"require_parameters": True}`, específico do endpoint Zen.
- Removidos headers não padrão do OpenRouter (`X-Title` e `HTTP-Referer`) das chamadas de chat.

### Added
- Adicionado header `x-opencode-session` nas requisições de chat, conforme recomendado pela documentação do OpenCode Go.
- Adicionado `.gitignore` para excluir `__pycache__`, arquivos `.pyc` e configurações de IDEs.

### Fixed
- Corrigida divergência de URL em `__init__.py`, que ainda usava o endpoint antigo `/zen/v1` hardcoded.
- Corrigido domínio do botão "My Home Assistant" no `README.md` (`opencode` → `open_code`).
- Corrigido nome do logger no template de bug report (`custom_components.opencode_ha` → `custom_components.open_code`).

## [1.0.3] e anteriores

- Versões originais do repositório `airy10/opencode_ha`.
- Veja o histórico original em: https://github.com/airy10/opencode_ha/releases

---

[1.0.41]: https://github.com/wesiofilhoIF/opencodeGO_ha/releases/tag/v1.0.41
[1.0.5]: https://github.com/wesiofilhoIF/opencodeGO_ha/releases/tag/v1.0.5
[1.0.4]: https://github.com/wesiofilhoIF/opencodeGO_ha/releases/tag/v1.0.4
[1.0.3]: https://github.com/airy10/opencode_ha/releases/tag/v1.0.3
